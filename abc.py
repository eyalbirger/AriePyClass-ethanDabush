import numpy as np
import random

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
m = len(x)

alpha = 0.0001
def calcJ(a, b):
    J = 0
    Da = 0
    Db = 0

    for i in range(m):
        J = J + (a*x[i] + b - y[i]) ** 2
        Da = Da + (a*x[i] + b - y[i]) * x[i] * 2
        Db = Db + (a*x[i] + b - y[i]) * 2

    return J/m, Da/m, Db/m

def train(iterations):
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)

    for i in range(iterations):
        J, Da, Db = calcJ(a, b)
        a -= Da*alpha
        b -= Db*alpha
    return a, b

A, B =train(1000000)
print("A = ", A)
print("B = ", B)