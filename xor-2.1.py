import math,random

b = [1]
inp1 = [0,1]
inp2 = [0,1]
x0 = [inp1,inp2,b]
w1 = [[0,0],[0,0],[0,0]]
w2 = [[0],[0]]
x1 = [0,0]
x2 = [0]

def multiplyMatrices(matrix1,matrix2):
    result = []
    for i in range(len(matrix1)):
        result.append([])
        for j in range(len(matrix1[0])):
            result[i].append(sum(matrix2[k][j]*matrix1[i][k] for k in range(len(matrix2))))
    return result
def activation(x):
    return 1/(1+math.e**(-x))



for x in [w1,w2]:
    for i in range(len(x)):
        for j in range(len(x[i])):
            x[i][j] = random.random()*2-1

error = 9999.9
while error>.005:
    for i in x0[0]:
        for j in x0[1]:
            for k in x0[2]:
                x1 = multiplyMatrices(x0,w1)
                print(x1)
                exit()