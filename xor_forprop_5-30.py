import math, sys, re, random

inp = [(0,0,1),(0,1,1),(1,0,1),(1,1,1)]
theOut = [0,1,1,0]                  # theoretical output
step = .1


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
def displayNN(errorlist, weights):
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

#function
def f(x):
    return 1/(1+math.e**(-x))

def deriv(x):
    return f(x)*(1-f(x))

def error(theOut,expOut,nnWeights):
    return [.5 * (theOut[i] - expOut[i]*nnWeights[2][0]) for i in range(len(expOut))]








# MAIN
# X01-inp1
# X00-inp2   0
# X10-bias   0   0

extractNNSpecs()
weights = randomWeights(3,2,1)
# weights in order of first half go to the top node
nnWeights = [[weights.pop(),weights.pop(),weights.pop(),weights.pop(),weights.pop(),weights.pop()],
             [weights.pop(),weights.pop()],[weights.pop()]]





#forwardpropogation
xvals = []
expOut = []
for i in inp:   # make 2nd layer
    node1,node2 = forwardNodes(i,nnWeights)
    expVal = dotProduct((node1,node2),nnWeights[1])
    xvals.append(expVal)
    expOut.append(expVal)


errorlist = error(theOut,expOut,nnWeights)

print(xvals)
displayNN(errorlist,nnWeights)

#backpropogation
# lasterror = [theOut[i]-expOut[i] for i in range(len(theOut))]
# error = [errorlist[i]*lasterror[i]*deriv(xvals[i]) for i in range(len(lasterror))]