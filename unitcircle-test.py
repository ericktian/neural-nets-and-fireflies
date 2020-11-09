import numpy as np
import random


# syn0array = [[-16.902669173023693, -22.235163842056092, -0.06071293554734092, 0.35558279005889953], [0.027854023254821052, -2.0656004376186514, 15.984893633030001, -12.825323452246845], [-12.057181451121938, 14.8883953082205, -12.376911708685327, -9.106254231718786]]
# syn1array = [[-36.962690520509604], [35.84300753846032], [-36.714820693618826], [-37.56901017105353]]
syn0array = [[0.8902890389154591, 1.3293843547346973, 19.252004933698547, 27.69359158677681], [19.67463097005881, -17.45319944679977, 0.852502584984745, -2.0879466166387974], [-15.691941244648648, -12.542892473331287, -14.364903298877714, 16.560160134789164]]
syn1array = [[-113.61669849220947], [-111.82420971618576], [-112.28099046233838], [109.99515805207507]]
syn0 = np.array(syn0array)
syn1 = np.array(syn1array)

numtest = 100000
def nonlin(x, deriv=False):
    if (deriv == True):
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))

inptest = []
outtest = []
for i in range(numtest):
    xval = random.random()*3 - 1.5
    yval = random.random()*3 - 1.5
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
toprint += 'Scaled score: ' + str(wrong/10)+' wrong out of '+str(numtest/10)+'\n'
toprint += str(100*(numtest-wrong)/numtest)+"%"+'\n'

toprint += '\nsyn0: '+str(syn0.tolist())+' \nsyn1: '+str(syn1.tolist())+'\n'
# toprint += '\nIterations: '+str(it)+' \n\n'
print(toprint)