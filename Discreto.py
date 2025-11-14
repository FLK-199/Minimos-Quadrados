import numpy as np
from sympy import *

x = Symbol('x')

fi = [x**0, x, x**2]
xi = [-1, 0, 1, 2]
yi = [0, -1, 0, 7]

a = np.zeros((len(fi), len(fi)))
b = np.zeros(len(fi))

def prodInt(i, j, c):
    prod = 0
    if c == 'a':
        for k in xi:
            prod += fi[i].subs(x, k)*fi[j].subs(x, k)
    if c == 'b':
        for k in range(0, len(yi)):
            prod += yi[k]*fi[i].subs(x, xi[k])
    return prod

for i in range(0, len(fi)):
    for j in range(0, len(fi)):
        a[i][j] = prodInt(i, j, 'a')

for i in range(0, len(fi)):
    b[i] = prodInt(i, 0, 'b')

print(a, "\n\n", b, "\n")

sol = np.linalg.solve(a, b)

print(sol)
