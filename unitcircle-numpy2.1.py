import numpy as np
import random, datetime

### supposed to keep testing until good dataset
file = open("unitcircle/lowest.out", "w")

numtrained = 100
numtest = 10000
trainerror = .05

np.random.seed(1)
syn0 = 2 * np.random.random((3, 4)) - 1
syn1 = 2 * np.random.random((4, 1)) - 1

import msvcrt
def kbfunc():
   x = msvcrt.kbhit()
   if x:
      ret = ord(msvcrt.getch())
   else:
      ret = 0
   return ret
def nonlin(x, deriv=False):
    if (deriv == True):
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))

toprintlowest = ""
currentwrong = 999999999
lowestwrong = currentwrong
broke = False
while True:#currentwrong>4000:
    if kbfunc():
        break

    inp = []
    out = []
    for x in range(numtrained):
        xval = random.random()*2.2 - 1.1
        yval = random.random()*2.2 - 1.1
        # xval = random.random()*3-1.5
        # yval = random.random()*3-1.5
        inp.append([xval,yval,1])
        if xval**2+yval**2<1:
            out.append([1])
        else:
            out.append([0])
    X = np.array(inp)
    y = np.array(out)


    error = 9999.9
    it = 0
    while error > trainerror:
        it+=1
        if it > 4000:
            broke = True
            break
        # print(it)
        l0 = X
        l1 = nonlin(np.dot(l0, syn0))
        l2 = nonlin(np.dot(l1, syn1))
        l2_error = y - l2
        # if it%100==0:
        # print("Error:" + str(np.mean(np.abs(l2_error))))
        error = np.mean(np.abs(l2_error))
        l2_delta = l2_error * nonlin(l2, deriv=True)
        l1_error = l2_delta.dot(syn1.T)
        l1_delta = l1_error * nonlin(l1, deriv=True)

        syn1 += l1.T.dot(l2_delta)
        syn0 += l0.T.dot(l1_delta)
    # print(it)
    if broke:
        broke = False
        print("over 4000 iterations\n")
        continue
    inptest = []
    outtest = []
    for i in range(numtest):
        xval = random.random()*4 - 2
        yval = random.random()*4 - 2
        inptest.append([xval,yval,1])
        if xval**2+yval**2<1:
            outtest.append([1])
        else:
            outtest.append([0])
    xtest = np.array(inptest)
    ytest = np.array(outtest)
    l0test = xtest
    l1test = nonlin(np.dot(l0test, syn0))
    l2test = nonlin(np.dot(l1test, syn1))
    # print(l2test.tolist())
    # print(ytest.tolist())
    expY = l2test.tolist()
    theY = ytest.tolist()
    wrong = 0
    for k in range(len(expY)):
        for o in range(len(expY[k])):
            if (expY[k][o]>.5 and theY[k][o]==0) or (expY[k][o]<.5 and theY[k][o]==1):
                wrong += 1
    toprint = ""
    toprint += str(wrong)+' wrong out of '+str(numtest)+'\n'
    toprint += str(100*(numtest-wrong)/numtest)+"%"+'\n'

    toprint += '\nsyn0: '+str(syn0.tolist())+' \nsyn1: '+str(syn1.tolist())+'\n'
    toprint += '\nIterations: '+str(it)+' \n\n'
    print(toprint)
    currentwrong = wrong
    if currentwrong<lowestwrong and it<=4000:
        file.write(toprint)
        lowestwrong = currentwrong
        toprintlowest = toprint
print('ended')
now = datetime.datetime.now()
newfile = open("unitcircle/"+str('%.3f' % (100*(numtest-lowestwrong)/numtest))+"%___"
               +str(now.year)+"-"+str(now.month)+"-"+str(now.day)+"_"
               +str(now.hour)+";"+str(now.minute)+";"+str(now.second)+".out", "w")
newfile.write(toprintlowest)