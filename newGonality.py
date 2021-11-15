# assume graph is an adjacency list of a simple graph as an array of sets, graph[0]={2,4,5}
import stateGraphs as sg
import itertools
import queue
import math
from networkx.classes.function import degree


def degreeList(graph):
    output=[]
    for a in graph:
        output.append(len(a))
    return output

#maybe pass the vertex with negative chips
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
        if c[v]<0:
            q.put(v)
            # go back and check if this is ever necessary for gonality game

    return (len(beenBorrowed)!=n)


def zeroIndex(state):
    output = []
    for i in range(1,1+len(state)):
        output.append({k-1 for k in state[i]})
    return output

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

def gonality(graph, startFrom=0):
    n=len(graph)
    degrees = degreeList(graph)
    minDegree = 10000000000
    for d in degrees:
        if d<minDegree:
            minDegree=d
    k=max(startFrom, minDegree)
    while True:
        for tup in itertools.combinations_with_replacement(range(0,k),n-1):
            wins = True
            d=[1+tup[0]]+[0]*(n-2)+[k-1-tup[-1]]
            for t in range(1,n-1):
                d[t]+=tup[t]-tup[t-1]
                
                # i added this and had it skip the rest if too many chips were on one
                # vertex, but it seemed to only make it slower :(
                #
                # if d[t]>=degrees[t]:
                #     wins=False
                #     break 
                 
            for i in range(1,n):
                if d[i]==0:
                    c=d.copy()
                    c[i]=-1
                    if not checkWinnable(c,graph,degrees):
                        wins=False
                        break
            if wins:
                print(d)
                return k
        k+=1





# print(gonality(zeroIndex(sg.TN)))
print(gonality(pruneLeaves(zeroIndex(sg.GA))))
# degrees = degreeList(graph)
# print(gonality(zeroIndex(sg.IL)))

# maybe tailor the function that checks if a divisor is winnable
# add progress updates in function
# ignore divisors that place more than the degree of the vertex (tried, maybe didn't help?)
