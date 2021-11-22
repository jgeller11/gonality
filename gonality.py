import stateGraphs as sg
import itertools
import queue
import networkx as nx
import math
import random 

# returns treewidth of a graph
def tw(graph):
    G = nx.Graph()
    for i in range(len(graph)):
        G.add_node(i)
    for i in range(len(graph)):
        for y in graph[i]:
            if i>y:
                G.add_edge(i,y)
    return max(nx.algorithms.approximation.treewidth_min_degree(G)[0],nx.algorithms.approximation.treewidth_min_fill_in(G)[0])

# returns list of the degrees of each vertex in a graph
def degreeList(graph):
    output=[]
    for a in graph:
        output.append(len(a))
    return output

# old winnable divisor checker
def checkWinnable(c, graph, degrees):
    n=len(c)
    q=queue.Queue(n)
    beenBorrowed=set()
    
    for i in range(n):
        if c[i]<0:
            q.put(i)
            beenBorrowed.add(i)
    
    while (not q.empty()) and len(beenBorrowed)<n:
        v=q.get()
        
        for neighbor in graph[v]:
            c[neighbor]-=1
            if c[neighbor] == -1:
                q.put(neighbor)
                beenBorrowed.add(neighbor)
        c[v]+=degrees[v]
        
    return (len(beenBorrowed)!=n)

# i got this to work and it was slightly faster, but q-reducing approach was faster than this
def checkWinnableSpecial(c, graph, degrees, v,n):
    # n=len(c)
    q=queue.Queue(n)
    beenBorrowed={v}

    for neighbor in graph[v]:
        c[neighbor]-=1
        if c[neighbor] == -1:
            q.put(neighbor)
            beenBorrowed.add(neighbor)
    c[v]+=degrees[v]
    while (not q.empty()):
        v=q.get()
        for neighbor in graph[v]:
            c[neighbor]-=1
            if c[neighbor] == -1:
                q.put(neighbor)
                beenBorrowed.add(neighbor)
                if len(beenBorrowed)==n:
                    return False
        c[v]+=degrees[v]
    return True

# checks if a divisor is q-reduced. if it isn't, it finds the largest valid firing set and fires it
def checkQReduced(c, graph, q, n):
    Q=queue.Queue(n)
    burnAdjacent=[0]*n
    burnt={q}
    for v in graph[q]:
        if v not in burnt:
            if c[v]<=burnAdjacent[v]:
                burnt.add(v)
                burnAdjacent[v]=0
                Q.put(v)
            else:
                burnAdjacent[v]+=1
    while not Q.empty():
        q=Q.get()
        for v in graph[q]:
            if v not in burnt:
                if c[v]<=burnAdjacent[v]:
                    burnt.add(v)
                    burnAdjacent[v]=0
                    Q.put(v)
                else:
                    burnAdjacent[v]+=1
    if len(burnt)!=n:
        for v in range(n):
            if burnAdjacent[v]>0:
                for w in graph[v]:
                    if w in burnt:
                        c[w]+=1
                c[v]-=burnAdjacent[v]
    return burnt
    
# sorts a graph so that maximum degree vertices are first–seems to be faster with how our current implementation works
def sortGraph(graph):
    degrees=[-1*i for i in degreeList(graph)]
    newOrder=list(range(len(graph)))
    newOrder = [x for _, x in sorted(zip(degrees, newOrder), key=lambda pair: pair[0])]
    output = []
    for i in range(len(newOrder)):
        output.append({newOrder.index(j) for j in graph[newOrder[i]]})
    return output

# cuts leaves off of a graph
def pruneLeaves(graph):
    i=0
    while i<len(graph) and len(graph)>1:
        if len(graph[i])<=1:
            for j in range(len(graph)):
                if i in graph[j]:
                        graph[j].remove(i)
                for k in range(i+1,len(graph)):
                    if k in graph[j]:
                        graph[j].remove(k)
                        graph[j].add(k-1)
            del graph[i]
            i=0
        else:
            i+=1
    return graph

# calculates gonality
def gonality(graph, startFrom=0, startFromConfig=0, progressUpdates=False):
    n=len(graph)

    k=max(startFrom, tw(graph))

    while True:
        count = 0
        if progressUpdates:
            
            print('Checking '+str(k),end='\r')
        for tup in itertools.combinations_with_replacement(range(0,k),n-1):
            
            count+=1
            
            if count>startFromConfig:
                
                if not(count%10000) and progressUpdates:
                    print('Checking '+str(k)+', at '+str(count)+'/'+str(int(math.factorial(k+n-2)/(math.factorial(k-1)*math.factorial(n-1)))),end='\r')
                wins = True
                
                d=[1+tup[0]]+[0]*(n-2)+[k-1-tup[-1]]
                # d=[tup[0]]+[0]*(n-2)+[k-tup[-1]]

                for t in range(1,n-1):
                    d[t]+=tup[t]-tup[t-1]

                for i in range(1,n):
                # for i in range(0,n-1):
                    if d[i]==0:
                        
                        # c=d.copy()
                        
                        # c[i]=-1

                        if not qReducedCheckWins(d.copy(), graph, i, n):
                            wins=False
                            break

                if wins:
                    print(d)
                    return k
        k+=1

# works from top down to randomly find divisors that win gonality game.
def randomGonalityUpperBound(graph,k=0):
    n=len(graph)
    if k==0:
        k=n
    
    while True:
        wins = True

        d=[1]+[0]*(n-1)

        for i in range(k):
            d[math.floor(random.random()*n)]+=1

        for i in range(1,n):
            if d[i]==0:
                
                c=d.copy()
                
                c[i]=-1

                if not qReducedCheckWins(c, graph, i, n):
                    wins=False
                    break

        if wins:
            print('upper bound of '+str(k)+': '+str(d))
            randomGonalityUpperBound(graph,k-1)


# checks if a divisor can move a chip to q
def qReducedCheckWins(c, graph, q, n):
    burnt = checkQReduced(c, graph, q, n)
    if len(burnt)==n:
        return False
    while c[q]<1:
        burnt = checkQReduced(c, graph, q, n)
        if len(burnt)==n:
            return False
    return True

