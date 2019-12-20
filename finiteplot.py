import matplotlib.pyplot as plt
import numpy as np

f = lambda x: 0.1*x**5 -0.2*x**3 + 0.1*x -0.2

h = 0.01
x = np.linspace(0,1,11)

print(x)
#central differnces approximation
dfc1 = (f(x+h) - f(x-h))/(2*h)
dfc2 = (f(x+h)- 2*f(x)+ f(x-h))/ h**2
print(dfc1)
print(dfc2)
