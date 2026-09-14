import numpy as np
import random

x = np.arange(27).reshape(9, 3)
y = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
#m = len(y)
#n = x.shape[0]

alpha = 0.0001
def calcJ(X,Y,W, b):

    n = X.shape[1]
    m = len(Y)

    J = 0
    DW = np.zeros(n)
    Db = 0
    
    for i in range(m):
        
        diff=0
        y_hat = b
        for j in range(n):
            y_hat+=W[j]*X[i,j]

        diff=y_hat-Y[i]
        
        J = J + diff ** 2
        Db = Db + diff * 2
        for j in range (n):
            DW[j] = DW[j] + diff * X[i,j] * 2


    return J/m, DW/m, Db/m

def train(X, Y, iterations, alpha):

    w = np.zeros(len(X[0]))
    for i in range(len(X[0])):
        w[i] = random.randint(-26, 26)

    b = random.randint(-10, 10)

    for i in range(iterations):
        J, Da, Db = calcJ(X, Y, w, b)
        w -= Da*alpha
        b -= Db*alpha
    return w, b

W, B = train(x, y, 1000000, alpha)
for i in range (len(W)):
    print(f"W={W[i]},", end=" ")
print()
print("B = ", B)