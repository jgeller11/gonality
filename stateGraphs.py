from gonalitysolver import *

# nested_dict = { 'dictA': {'key_1': 'value_1'},
#                 'dictB': {'key_2': 'value_2'}}



# points are not borders!!!!! leads to nonplanar graphs

def dictToGraph(d):
    n = len(d)
    graph = [[0 for k in range(n)] for l in range(n)]
    for i in range(1,n+1):
        for j in d[i]:
            graph[i-1][j-1]=1
    return graph

def pruneLeaves(g):
    n = len(g)
    for i in range(n):
        deg = 0
        for j in range(n):
            deg += g[i][j]
        if deg == 1:
            del g[i]
            for row in g:
                del row[i]
            return pruneLeaves(g)
    return g

def check(d):
    for i in range (1,len(d)+1):
        for j in range(1,len(d)+1):
            if i in d[j] and not (j in d[i]):
                print('mismatch at '+str(i)+', '+str(j))
                return True
    for i in range(1, len(d)+1):
        if i in d[i]:
            print(str(i)+' points at self')
            return True
    # print('all good!')
    return False

# todo:
#   - write up rest of states
#   - implement f to create adj. matrices
#   - implement f to prune leaves
#   - implement checks to never place more chips than degree
#       - coulld just be an if statement, should be clever selection

abbreviationStrings=['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']

AL = {
    1: {2, 7},
    2: {1, 3, 6, 7},
    3: {2, 4, 6},
    4: {3, 5, 6, 7},
    5: {4},
    6: {2, 3, 4, 7},
    7: {1, 2, 4, 6}
}
AK = {
    1: set()
}
AZ = {
    1: {2, 3, 4, 5, 7, 9},
    2: {1, 3},
    3: {1, 2, 4, 7, 8},
    4: {1, 3, 5, 6, 8},
    5: {1, 4, 6, 9},
    6: {4, 5, 7, 8, 9},
    7: {1, 3, 6, 8, 9},
    8: {3, 4, 6, 7},
    9: {1, 5, 6, 7}
}
AR = {
    1: {2, 3, 4},
    2: {1, 3, 4},
    3: {1, 2, 4},
    4: {1, 2, 3}
}
#CA!
CA = {
}
CO = {
    1: {2, 4, 6, 7},
    2: {1, 3, 4, 5, 6, 7},
    3: {2, 4, 5},
    4: {1, 2, 3, 5, 6},
    5: {2, 3, 4},
    6: {1, 2, 4, 7},
    7: {1, 2, 6}
}
CT = {
    1: {2,3,5},
    2: {1,3},
    3: {1,2,4,5},
    4: {3,5},
    5: {1,3,4}
}
DE = {
    1: set()
}
FL = {
    1: {2},
    2: {1, 3, 5, 11},
    3: {2, 4, 5, 6, 11},
    4: {3, 5, 6},
    5: {2, 3, 4},
    6: {3, 4, 7, 8, 10, 11},
    7: {6, 8, 9, 10},
    8: {6, 7, 9, 17, 18},
    9: {7, 8, 10, 15, 17},
    10: {6, 7, 9, 11, 15},
    11: {2, 3, 6, 10, 12, 15},
    12: {11, 13, 14, 15},
    13: {12, 14, 16},
    14: {12, 13, 15, 16},
    15: {9, 10, 11, 12, 14, 16, 17},
    16: {13, 14, 15, 17},
    17: {8, 9, 15, 16, 18, 19, 25},
    18: {8, 17, 20, 21},
    19: {17, 25},
    20: {18, 21, 22, 23, 24, 25},
    21: {18, 20, 22},
    22: {20, 21, 23},
    23: {20, 22, 24, 27},
    24: {20, 23, 25, 27},
    25: {17, 19, 20, 24, 26, 27},
    26: {25, 27},
    27: {23, 24, 25, 26}   
}
GA = {
    1: {8, 12},
    2: {3, 8},
    3: {2, 8, 10, 13, 14},
    4: {5, 6, 7, 10, 13},
    5: {4, 6, 11, 13},
    6: {4, 5, 7, 11},
    7: {4, 6, 9, 10, 11},
    8: {1, 2, 3, 10, 12},
    9: {7, 10, 11, 14},
    10: {3, 4, 7, 8, 9, 12, 13},
    11: {5, 6, 7, 9, 13, 14},
    12: {1, 8, 10},
    13: {3, 4, 5, 10, 11, 14},
    14: {3, 9, 11, 13}
}
HI = {
    1: {2},
    2: {1}
}
ID = {
    1: {2},
    2: {1}
}
IL = {
    1: {2, 3, 7, 11, 16},
    2: {1, 16},
    3: {1, 4, 5, 6, 7, 11},
    4: {3, 5, 7},
    5: {3, 4, 6, 7, 8, 9},
    6: {3, 5, 8, 10, 11, 14},
    7: {1, 3, 4, 5},
    8: {5, 6, 9, 10},
    9: {5, 8, 10},
    10: {6, 8, 9, 14},
    11: {1, 3, 6, 14, 16},
    12: {13, 15},
    13: {12, 15, 18},
    14: {6, 10, 11, 16},
    15: {12, 13, 16, 18},
    16: {1, 2, 11, 14, 15, 17, 18},
    17: {16, 18},
    18: {13, 15, 16, 17}
}
IN = {
    1: {2, 4},
    2: {1, 3, 4, 5},
    3: {2, 5, 6},
    4: {1, 2, 5, 6, 7, 8, 9},
    5: {2, 3, 4, 6, 7},
    6: {3, 4, 5, 7, 9},
    7: {4, 5, 6},
    8: {4, 9},
    9: {4, 6, 8}
}
IA = {
    1: {2, 4},
    2: {1, 3, 4},
    3: {2, 4},
    4: {1, 2, 3}
}
KS = {
    1: {2, 4},
    2: {1, 3, 4},
    3: {2},
    4: {1, 2}
}
KY = {
    1: {2, 5},
    2: {1, 3, 4, 5, 6},
    3: {2, 4},
    4: {2, 3, 5, 6},
    5: {1, 2, 4, 6},
    6: {2, 4, 5}
}
LA = {
    1: {2, 5, 6},
    2: {1, 6},
    3: {4, 5, 6},
    4: {3, 5},
    5: {1, 3, 4, 6},
    6: {1, 2, 3, 5}
}
ME = {
    1: {2},
    2: {1}
}
MD = {
    1: {2, 7, 8},
    2: {1, 3, 7},
    3: {2, 4, 7, 8},
    4: {3, 5, 8},
    5: {4},
    6: {8},
    7: {1, 2, 3, 8},
    8: {1, 3, 4, 6, 7}
}
MA = {
    1: {2},
    2: {1, 3, 4, 5},
    3: {2, 5, 6},
    4: {2, 5, 7, 8, 9},
    5: {2, 3, 4, 6, 7},
    6: {3, 5},
    7: {4, 5, 8},
    8: {4, 7, 9},
    9: {4, 8}
}
MI = {
    1: {2, 4, 5},
    2: {1, 3, 4, 6},
    3: {2, 4, 6, 7},
    4: {1, 2, 3, 5, 7, 8},
    5: {1, 4, 8, 10},
    6: {2, 3, 7},
    7: {3, 4, 6, 8, 11, 12},
    8: {4, 5, 7, 10, 11},
    9: {10, 11, 14},
    10: {5, 8, 9, 11},
    11: {7, 8, 9, 10, 12, 13, 14},
    12: {7, 11, 13},
    13: {11, 12, 14},
    14: {9, 11, 13}
}
MN = {
    1: {2, 7},
    2: {1, 3, 4, 5, 6, 7},
    3: {2, 5, 6},
    4: {2, 5, 6},
    5: {2, 3, 4, 6},
    6: {2, 3, 4, 5, 7, 8},
    7: {1, 2, 6, 8},
    8: {6, 7}
}
MS = {
    1: {2, 3},
    2: {1, 3},
    3: {1, 2, 4},
    4: {3}
}
MO = {
    1: {2, 3},
    2: {1, 3},
    3: {1, 2, 4, 6, 8},
    4: {3, 5, 6, 7, 8},
    5: {4, 6},
    6: {3, 4, 5},
    7: {4, 8},
    8: {3, 4, 7}
}
MT = {
    1: set()
}
NE = {
    1: {2, 3},
    2: {1, 3},
    3: {1, 2}
}
NV = {
    1: {3, 4},
    2: {4},
    3: {1, 4},
    4: {1, 2, 3}
}
NH = {
    1: {2},
    2: {1}
}
NJ = {
    1: {2, 3},
    2: {1, 3},
    3: {1, 2, 4},
    4: {3, 6, 12},
    5: {7, 9, 11},
    6: {4, 7, 10, 12},
    7: {5, 6, 10, 11, 12},
    8: {9, 10, 11},
    9: {5, 8, 11},
    10: {6, 7, 8, 11},
    11: {5, 7, 8, 9, 10},
    12: {4, 6, 7}
}
NM = {
    1: {2, 3},
    2: {1, 3},
    3: {1, 2}
}
#NY!
NY = {
}
#NC!
NC = {
}
ND = {
    1: set()
}
#OH!
OH = {
}
OK = {
    1: {2, 3},
    2: {1, 3, 4, 5},
    3: {1, 2, 4, 5},
    4: {2, 3, 5},
    5: {2, 3, 4}
}
OR = {
    1: {3, 5},
    2: {3, 4, 5},
    3: {1, 2, 5},
    4: {2, 5},
    5: {1, 2, 3, 4}
}
#PA!
PA = {
}
RI = {
    1: {2},
    2: {1}
}
SC = {
    1: {6, 7},
    2: {3, 5, 6},
    3: {2, 4, 5},
    4: {3, 5},
    5: {2, 3, 4, 6, 7},
    6: {1, 2, 5, 7},
    7: {1, 5, 6}
}
SD = {
    1: set()
}
TN = {
    1: {2},
    2: {1, 3},
    3: {2, 4, 6},
    4: {3, 5, 6, 7},
    5: {4, 6, 7},
    6: {3, 4, 5, 7},
    7: {4, 5, 6, 8},
    8: {7, 9},
    9: {8}
}
#TX!
TX = {
}
UT = {
    1: {2, 3},
    2: {1, 3, 4},
    3: {1, 2, 4},
    4: {2, 3}
}
VT = {
    1: set()
}
#VA!
VA = {
}
WA = {
    1: {2, 4, 7, 8, 9},
    2: {1, 6, 7},
    3: {4, 6, 8, 10},
    4: {1, 3, 5, 8},
    5: {4},
    6: {2, 3, 7, 9, 10},
    7: {1, 2, 6, 9},
    8: {1, 3, 4, 9, 10},
    9: {1, 6, 7, 8, 10},
    10: {3, 6, 8, 9}
}
WV = {
    1: {2},
    2: {1, 3},
    3: {2}
}
WI = {
    1: {2, 4, 5},
    2: {1, 3, 5, 6},
    3: {2, 6, 7, 8},
    4: {1, 5, 6},
    5: {1, 2, 4, 6},
    6: {2, 3, 4, 5, 8},
    7: {3, 8},
    8: {3, 6, 7}
}
WY = {
    1: set()
}

states=[AL,AK,AZ,AR,CA,CO,CT,DE,FL,GA,HI,ID,IL,IN,IA,KS,KY,LA,ME,MD,MA,MI,MN,MS,MO,MT,NE,NV,NH,NJ,NM,NY,NC,ND,OH,OK,OR,PA,RI,SC,SD,TN,TX,UT,VT,VA,WA,WV,WI,WY]

# for c in range(len(abbreviations)):
#     if check(abbreviations[c]):
#         print(abbreviationStrings[c])

# print(dictToGraph(WA))
# print(pruneLeaves(dictToGraph(WA)))

print(str( gonalityUpperBound(pruneLeaves(dictToGraph(FL)),False)))

# for s in range(len(states)):
#     if len(states[s])==1 or len(pruneLeaves(dictToGraph(states[s])))==1:
#         print(abbreviationStrings[s]+': 1')
#     elif len(states[s])>1 and len(states[s])<15:
#         print(abbreviationStrings[s]+': '+str( findGonalityFaster(pruneLeaves(dictToGraph(states[s])),True)))

# check(CO)

# 1: {},
# 2: {},
# 3: {},
# 4: {},
# 5: {},
# 6: {},
# 7: {},
# 8: {},