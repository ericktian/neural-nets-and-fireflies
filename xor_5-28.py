import math, sys, re, random

# FUNCTIONS

#1
def extractNNSpecs():
    args = sys.argv[1:]               # command line arguments
    if len(args)<1 or re.compile("^\\d+$").search(args[-1]) is not None:
        args += [sys.argv[0] + "..\\..\\XOR.txt"]   # append the ...
    fileLoc = args[-1]                # training set location
    aTraining = open(fileLoc, "r").read().splitlines()  # make a list of the training set
    aInitial, aFinal = [], []         # We'll separate the input and output
    for idx in range(len(aTraining)): # For each training set item
        strIn, strOut = aTraining[idx].split(" => ")  # separate it into input and output
        # print ("'{}' ==> '{}'".format(strIn, strOut))
        aInitial.append([float(mynum) for mynum in re.split(  # make each input part numeric
          "\\s+,?\\s*|\\s*,?\\s+", strIn.strip())] + [1.0])   # trailing element is bias
        aFinal.append  ([float(mynum) for mynum in re.split(  # make each output part numeric
          "\\s+,?\\s*|\\s*,?\\s+", strOut.strip())])
    # Fix the number of nodes per each layer
    aLayerCt = [len(aInitial[0])] + [int(n) for n in args[:-1]] + [len(aFinal[0])]
    return aInitial, aFinal, aLayerCt

#2
def randomWeights(numIn,numLayer,numOut):
    weights = set()
    numWeights = (numIn*numLayer)+(numLayer*numOut)+numOut
    for i in range(numWeights):
        weights.add(random.random()*2-1)
    return weights

#3
def dotProduct(vector1,vector2):
    return sum(i[0]*i[1] for i in zip(vector1,vector2))

#4
def displayNN(inp, theOut, weights):
    expOut = []
    for i in inp:   # make 2nd layer
        node1,node2 = forwardNodes(i,weights)
        expVal = dotProduct((node1,node2),weights[1])
        expOut.append(expVal)

    errorlist = [.5*(theOut[i]-expOut[i]*weights[2][0]) for i in range(len(expOut))]

    print('Total error:',sum(errorlist))
    print('Individual errors:',errorlist)
    print('Weights:',weights)
    print()

#5
def forwardNodes(i,weights):
    node1 = dotProduct(i, weights[0][:3])
    node2 = dotProduct(i, weights[0][3:])
    return (node1,node2)

#6
theOut = [0,1,1,0]                  # theoretical output

#7
lasterror = []
error =


# MAIN
# X01
# X00   0
# X10   0   0
inp = [(0,0,1),(0,1,1),(1,0,1),(1,1,1)]

extractNNSpecs()
weights = randomWeights(3,2,1)
# weights in order of first half go to the top node
nnWeights = [[weights.pop(),weights.pop(),weights.pop(),weights.pop(),weights.pop(),weights.pop()],
             [weights.pop(),weights.pop()],[weights.pop()]]
displayNN(inp,theOut,nnWeights)

