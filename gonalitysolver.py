import copy
import numpy as np
import itertools

# generates a list for each vertex which is the divisor reached from the all-zero
#   divisor by firing that vertex.

def genFirelist(graph, getMinDegree=False):
    fireList = copy.deepcopy(graph)
    mindegree=0
    for r in range(len(fireList)):
        t=0
        for i in range(len(fireList[r])):
            t-=fireList[r][i]
        fireList[r][r]=t
        if t>mindegree:
            mindegree=t
    if getMinDegree:
        return fireList, mindegree
    return fireList

# returns true if a divisor is effective

def effective(divisor):
    for d in range(len(divisor)):
        if divisor[d]<0:
            return d
    return -1

# returns true if a given divisor is solvable on a graph

def solveDivisor(graph, divisor):
    n = len(graph)
    unfired = set()
    fireList=genFirelist(graph)
    next = effective(divisor)
    while next != -1:
        unfired.add(next)
        if len(unfired)==n:
            return False
        for d in range(len(divisor)):
            divisor[d]-=fireList[next][d]
        next = effective(divisor)
    return True

# https://stackoverflow.com/questions/53561814/python-stars-and-bars

def placements(n,k):
    bars = [0 for i in range(n)]+[k+n]
    return [[bars[j+1] - bars[j] - 1 for j in range(n)] for bars[1:-1] in itertools.combinations(range(1, k+n), n-1)]


# greedy algorithm with very little optimization
def findGonality(graph):
    n = len(graph)
    for k in range(1,n):
        P = placements(n,k)
        for p in P:
            acceptable = True
            for i in range(len(p)):
                if acceptable:
                    if p[i]==0:
                        tp = p.copy()
                        tp[i]-=1
                        if not solveDivisor(graph, tp):
                            acceptable=False
            if acceptable:
                return k
    return 0

#technically takes symmetry as a parameter, but i think setting it to True only makes it slower

# works similarly to findGonality, but track states seen so far in sets of "solvable" and "nonsolvable" to speed up calculations

def findGonalityFaster(graph, symmetry=False):
    n = len(graph)
    fireList, mindegree=genFirelist(graph, True)
    for k in range(mindegree,n):
        solvable = set()
        unsolvable = set()
        P = placements(n,k)
        for p in P:
            acceptable = True
            for i in range(len(p)):
                if acceptable:
                    if p[i]==0:
                        tp = p.copy()
                        tp[i]-=1
                        current = set()
                        unfired = set()
                        next = effective(tp)
                        while next > -1:
                            if tuple(tp) in solvable:
                                next = -1
                            elif tuple(tp) in unsolvable:
                                next = -2
                                acceptable = False
                                unsolvable |= current
                            else:
                                if symmetry:
                                    for i in range(len(tp)):
                                        current.add(tuple(tp[i:]+tp[:i]))
                                else:
                                        current.add(tuple(tp))
                                unfired.add(next)
                                if len(unfired)==n:
                                    acceptable = False
                                    next = -2
                                    unsolvable |= current
                                else:
                                    for d in range(len(tp)):
                                        tp[d]-=fireList[next][d]
                                    next = effective(tp)
                        if next == -1:
                            solvable |= current

            if acceptable:
                return k
    return 0

# these functions all just generate adjacency matrices for different families of graphs

def genCycleGraph(n):
    row = [0 for i in range(n)]
    output = [copy.deepcopy(row) for i in range(n)]
    for i in range(n):
        output[i][i-1]=1
        output[i-1][i]=1
    return output

def genCompleteGraph(n):
    row = [1 for i in range(n)]
    output = [copy.deepcopy(row) for i in range(n)]
    for i in range(n):
        output[i][i]=0
    return output

def genAntiPrismGraph(n):
    row = [0 for i in range(2*n)]
    output = [copy.deepcopy(row) for i in range(2*n)]
    for i in range(n):
        output[i][(i+1)%n]=1
        output[(i+1)%n][i]=1
        output[i+n][((i+1)%n)+n]=1
        output[((i+1)%n)+n][i+n]=1
        output[i][i+n]=1
        output[i+n][i]=1
        output[i][((i+1)%n)+n]=1
        output[((i+1)%n)+n][i]=1
    return output

def genGridGraph(m,n):
    output = [[0 for i in range(n*m)] for j in range(n*m)]
    for i in range(m-1):
        for j in range(n):
            output[j*m+i][j*m+i+1]=1
            output[j*m+i+1][j*m+i]=1
    for j in range(n-1):
        for i in range(m):
            output[j*m+i][j*m+i+m]=1
            output[j*m+i+m][j*m+i]=1
    return output

def genHypercubeGraph(n):
    output = [[0 for i in range(1<<n)] for i in range(1<<n)]
    for i in range(1<<n):
        for j in range(i):
            fails=0
            k=0
            while k<n and fails<2:
                if (1&(i>>k))!=(1&(j>>k)):
                    fails+=1
                k+=1
            if fails==1:
                output[i][j]=1
                output[j][i]=1
    return output


# graphs should be given to functions as adjacency matrices, so
#
# C = [[0,1,1],[1,0,1],[1,1,0]]
# is a cycle on three vertices, and
# d = [2,1,-1]
# is a divisor that places 2, 1, and -1 chips on the first, second, and third vertices respectively

print(findGonalityFaster(genCompleteGraph(10)))
