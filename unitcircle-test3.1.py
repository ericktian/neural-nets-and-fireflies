import numpy as np
import random


# syn0array = [[-16.902669173023693, -22.235163842056092, -0.06071293554734092, 0.35558279005889953], [0.027854023254821052, -2.0656004376186514, 15.984893633030001, -12.825323452246845], [-12.057181451121938, 14.8883953082205, -12.376911708685327, -9.106254231718786]]
# syn1array = [[-36.962690520509604], [35.84300753846032], [-36.714820693618826], [-37.56901017105353]]
# syn0array= [[-27.263915515872853, -6.995159970957174, 24.709379713170144, -12.447098966082187, 17.24295867911108, -14.3897262979056], [-7.371714066402879, -26.74652882790786, -22.53689143660933, -41.62964980646496, 6.632753902724631, 17.652600865702325], [-25.053014739001412, -23.1400540236604, -29.801841143991552, 39.41039148952101, -15.903749597715306, -19.987906937389248]]
# syn1array= [[-40.53353424380038], [-39.482102293180795], [-41.76078922039539], [38.668789248475804], [-42.318759579820494], [-42.43804333387029]]
syn0array= [[24.00683169042202, 34.84162422162565, -23.36517387623072, -28.4023989890425, -33.01749905198405, -37.757041817091455, -2.847229010630212, 24.794759185000604, 4.464450651091788, 5.066736830796913], [26.736818011418162, 7.245049964158923, -29.418023623372314, 24.036615317668506, 24.549047868081846, -4.074117598070369, 35.712273923108405, -3.095686675623339, -31.492823280318223, 29.34709923238726], [-32.90703363318081, -33.38305211502643, -34.827707796506346, -34.74516037393459, 37.97734139847005, -35.013404948682314, -34.28602394891025, -23.796158473434755, -29.54773383002259, -23.142726335276354]]
syn1array= [[-17.424921837771358], [-21.4132442733534], [-28.46914374169137], [-28.478249627460215], [26.193299494654212], [-28.15549399500003], [-17.45108529593681], [-10.640374560776754], [-28.883171244712294], [-11.396951727034777]]
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