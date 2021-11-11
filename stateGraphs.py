import networkx as nx
import matplotlib.pyplot as plt

def graphState(state, planar=True):
    G = nx.Graph()
    for i in range(len(state)):
        G.add_node(i+1)
    for x in state:
        for y in state[x]:
            G.add_edge(x,y)
    if planar:
        pos = nx.planar_layout(G)
        nx.draw(G, with_labels=True, font_weight='bold', pos=pos)
    else:
        nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()


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
    return False

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
CA = {
    1: {2, 3, 4},
    2: {1, 3, 5},
    3: {1, 2, 4, 5, 6, 7, 9},
    4: {1, 3, 6, 7, 8, 9, 10, 16, 22, 23},
    5: {2, 3, 11},
    6: {3, 4, 7},
    7: {3, 4, 6, 9},
    8: {4, 23, 25, 27, 31, 36},
    9: {3, 4, 7, 10, 11, 15},
    10: {4, 9, 15, 16, 19},
    11: {5, 9, 13, 15},
    12: {14},
    13: {11, 15},
    14: {12, 18},
    15: {9, 10, 11, 13, 17, 19},
    16: {4, 10, 19, 20, 21, 22},
    17: {15, 18, 19},
    18: {14, 17, 19, 20},
    19: {10, 15, 16, 17, 18, 20},
    20: {16, 18, 19, 21, 24},
    21: {16, 20, 22, 23, 24},
    22: {4, 16, 21, 23},
    23: {4, 8, 21, 22, 24, 25},
    24: {20 , 21, 23, 25, 26},
    25: {8, 23, 24, 26, 27, 28, 29, 30},
    26: {24, 25, 30, 33},
    27: {8, 25, 28, 31, 32, 34, 35, 38, 40},
    28: {25, 27, 29, 30, 33, 34},
    29: {25, 28, 30},
    30: {25, 26, 28, 29, 33},
    31: {8, 27, 35, 36, 41},
    32: {27, 35, 38, 39},
    33: {26, 28, 30, 34, 37, 43, 44},
    34: {27, 28, 33, 37, 40},
    35: {27, 31, 32, 39, 41, 42},
    36: {8, 31, 41, 42, 50, 51},
    37: {33, 34, 40, 43},
    38: {27, 32, 39, 40, 44, 47},
    39: {32, 35, 38, 42, 45, 46, 47},
    40: {27, 34, 37, 38, 43, 44},
    41: {31, 35, 36, 42},
    42: {35, 36, 39, 41, 45, 49, 50},
    43: {33, 37, 40, 44},
    44: {33, 38, 40, 43, 47},
    45: {39, 42, 46, 48, 49},
    46: {39, 45, 47, 48},
    47: {38, 39, 44, 46, 48},
    48: {45, 46, 47, 49},
    49: {42, 45, 48, 50, 52},
    50: {36, 42, 49, 51, 52, 53},
    51: {36, 50, 53},
    52: {49, 50, 53},
    53: {50, 51, 52}
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
NY = {
    1: {2, 3},
    2: {1, 3, 4},
    3: {1, 2, 4, 5, 6, 14},
    4: {2, 3, 5},
    5: {3, 4, 6, 7, 8},
    6: {3, 5, 7, 12, 14},
    7: {5, 6, 8, 9, 10, 11, 12},
    8: {5, 7, 9, 11},
    9: {7, 8, 10, 11},
    10: {7, 9, 11, 12, 13},
    11: {7, 8, 9, 10},
    12: {6, 7, 10, 13, 14},
    13: {10, 12, 14, 15, 16},
    14: {3, 6, 12, 13, 15, 16},
    15: {13, 14},
    16: {13, 14, 17},
    17: {16, 18},
    18: {17, 19},
    19: {18, 20, 21, 22},
    20: {19, 21},
    21: {19, 20, 22},
    22: {19, 21, 23, 24},
    23: {22, 24, 27},
    24: {22, 23, 25, 27},
    25: {24, 27},
    26: {27},
    27: {23, 24, 25, 26}
}
NC = {
    1: {3, 4, 7},
    2: {4, 7, 8},
    3: {1, 7},
    4: {1, 2, 7, 8, 13},
    5: {10, 11, 12},
    6: {10, 13},
    7: {1, 2, 3, 4, 8, 9},
    8: {2, 4, 7, 9, 10, 12, 13},
    9: {7, 8, 12},
    10: {5, 6, 8, 12, 13},
    11: {5},
    12: {5, 8, 9, 10},
    13: {4, 6, 8, 10}
}
ND = {
    1: set()
}
OH = {
    1: {2, 8, 10, 15},
    2: {1, 6, 15},
    3: {12, 15},
    4: {5, 7, 8, 9, 12, 15},
    5: {4, 8, 9},
    6: {2, 7, 12, 13, 15},
    7: {4, 6, 9, 12, 13, 16},
    8: {1, 4, 5, 10, 15},
    9: {4, 5, 7, 11, 16},
    10: {1, 8, 15},
    11: {9, 13, 14, 16},
    12: {3, 4, 6, 7, 15},
    13: {6, 7, 11, 14, 16},
    14: {11, 13},
    15: {1, 2, 3, 4, 6, 8, 10, 12},
    16: {7, 9, 11, 13}
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
PA = {
    1: {2, 4, 7},
    2: {1, 3, 4},
    3: {2, 4, 5},
    4: {1, 2, 3, 5, 6, 7, 9},
    5: {3, 4, 6},
    6: {4, 5, 9, 11},
    7: {1, 4, 8, 9},
    8: {7, 9, 12},
    9: {4, 6, 7, 8, 10, 11, 12},
    10: {9, 11, 12, 13},
    11: {6, 9, 10, 13},
    12: {8, 9, 10, 13, 15},
    13: {10, 11, 12, 14, 15},
    14: {13, 15, 17, 18},
    15: {12, 13, 14, 16, 17},
    16: {15, 17},
    17: {14, 15, 16, 18},
    18: {14, 17}
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
TX = {
    1: {4, 5, 8, 36},
    2: {7, 8, 9, 10, 18, 29, 36},
    3: {4, 24, 26, 32},
    4: {1, 3, 5, 13, 26, 32},
    5: {1, 4, 6, 8, 17, 30, 32},
    6: {5, 12, 17, 25, 30, 33},
    7: {2, 9, 10, 22},
    8: {1, 2, 5, 10, 17, 36},
    9: {2, 7, 18, 22, 29},
    10: {2, 7, 8, 17, 22, 25, 27, 31, 35},
    11: {12, 13, 19, 21, 23, 25},
    12: {6, 11, 13, 24, 25, 26, 33},
    13: {4, 11, 12, 19, 26},
    14: {22, 27, 36},
    15: {27, 28, 34, 35},
    16: {23},
    17: {5, 6, 8, 10, 25, 31},
    18: {2, 9, 29},
    19: {11, 13},
    20: {21, 23, 35},
    21: {11, 20, 23, 25, 35},
    22: {7, 9, 10, 14, 27, 29, 36},
    23: {11, 16, 20, 21, 28, 35},
    24: {3, 12, 26, 30, 32, 33},
    25: {6, 10, 11, 12, 17, 21, 31, 35},
    26: {3, 4, 12, 13, 24},
    27: {10, 14, 15, 22, 34, 35},
    28: {15, 23, 35},
    29: {2, 9, 18, 22, 36},
    30: {5, 6, 24, 32, 33},
    31: {10, 17, 25},
    32: {3, 4, 5, 24, 30},
    33: {6, 12, 24, 30},
    34: {15, 27},
    35: {10, 15, 20, 21, 23, 25, 27, 28},
    36: {1, 2, 8, 14, 22, 29}
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
VA = {
    1: {2, 4, 5, 7, 10, 11},
    2: {1, 3, 4},
    3: {2, 4},
    4: {1, 2, 3, 5, 7},
    5: {1, 4, 6, 7, 9, 10},
    6: {5, 9, 10},
    7: {1, 4, 5},
    8: {10, 11},
    9: {5, 6},
    10: {1, 5, 6, 8, 11},
    11: {1, 8, 10}
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

abbreviationStrings=['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']
states=[AL,AK,AZ,AR,CA,CO,CT,DE,FL,GA,HI,ID,IL,IN,IA,KS,KY,LA,ME,MD,MA,MI,MN,MS,MO,MT,NE,NV,NH,NJ,NM,NY,NC,ND,OH,OK,OR,PA,RI,SC,SD,TN,TX,UT,VT,VA,WA,WV,WI,WY]