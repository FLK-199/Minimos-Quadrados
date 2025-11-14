import numpy as np
from sympy import *

x = Symbol('x')

fi = [x**0, x, x**2]
xi = [-1, 1]
f = x**4 - 5*x

a = np.zeros((len(fi), len(fi)))
b = np.zeros(len(fi))

def prodInt(i, j, c):
    prod = 0
    if c == 'a':
        prod = integrate(fi[i]*fi[j], (x, xi[0], xi[1]))
    if c == 'b':
        prod = integrate(fi[i]*f, (x, xi[0], xi[1]))

    return prod

for i in range(0, len(fi)):
    for j in range(0, len(fi)):
        a[i][j] = prodInt(i, j, 'a')

for i in range(0, len(fi)):
    b[i] = prodInt(i, 0, 'b')

print(a, "\n\n", b, "\n")

sol = np.linalg.solve(a, b)

print(sol)
