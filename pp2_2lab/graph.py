import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

x = np.linspace(-10,10,N)
N = 100

yarray = []

def f(x):
    return x**2

for i in x :
    y = f(i)
    yarray.append(y)

print(yarray)


E = integrate.simps(yarray,x)
print(E)

plt.plot(x,E)