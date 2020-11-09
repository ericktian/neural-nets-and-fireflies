#
# Erick Tian

import math,random

b = 1
# nodes = [[[b],[0],[0]],                                 # [layer][node]
#          [[0],[0]],
#          [[0]]]
nodes = [0,0,b,0,0,0]
# prevNodes = [[],[],[],                                  # fixed
#              [(0,0),(0,1),(0,2)],[(0,0),(0,1),(0,2)],   # [layer][node]
#              [(1,0),(1,1)]]
prevNodes = [[],[],[],[0,1,2],[0,1,2],[3,4]]
# nodeToNum = [[[0],[1],[2]],[[3],[4]],[5]]               # converts matrix to weights
# weights = [[0,0,0,0,0,0],                               #
#            [0,0]]

weights = [[-1,-1,0,0],[-1,-1,0,0],[-1,-1,0,0],         # -1 means weight DNE, 0 means weight exists
           [-1,-1,-1,-1,0],[-1,-1,-1,-1,0]]             # [prevnode][currentnode]


#    0[0][0]
#    1[0][1]  3[1][0]
# (b)2[0][2]  4[1][1]  5[2][0]

def initialize():
    return set(random.random()*2-1 for i in range(8))
def activation(x):
    return 1/(1+math.e**(-x))
def forward(a):                   # calculates forwardpropogation for node a
    return activation(sum([weights[i][a] for i in prevNodes[a]]))


### MAIN ###

randWeights = initialize()
for i in range(len(weights)):
    for j in range(len(weights[i])):
        if weights[i][j]==0:
            weights[i][j] = randWeights.pop()

