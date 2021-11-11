import stateGraphs as sg
import gonalitysolver as gs
# todo:
#   - write up rest of states
#   - implement f to create adj. matrices
#   - implement f to prune leaves
#   - implement checks to never place more chips than degree
#       - coulld just be an if statement, should be clever selection
#   - analyze by contracting bridges in some clever way?



# for c in range(len(states)):
#     if check(states[c]):
#         print(abbreviationStrings[c])

# print(dictToGraph(WA))
# print(pruneLeaves(dictToGraph(WA)))

# print(str( gonalityUpperBound(pruneLeaves(dictToGraph(FL)),16,False)))
# print(str( gs.randomGonalityUpperBound(pruneLeaves(dictToGraph(FL)),12,True)))

# for s in range(len(states)):
#     # if len(states[s])==1 or len(pruneLeaves(dictToGraph(states[s])))==1:
#         # print(abbreviationStrings[s]+': 1')
#     if len(states[s])>14 and len(states[s])<20:
#         print(abbreviationStrings[s]+': '+str(gs.findGonalityFaster(pruneLeaves(dictToGraph(states[s])),True)))

# print(str( gs.randomGonalityUpperBound(pruneLeaves(dictToGraph(NY)),9,True)))
# print(str( gs.findGonalityFaster(pruneLeaves(dictToGraph(NY)),0,True)))




sg.graphState(sg.IL, False)