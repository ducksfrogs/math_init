f = lambda x: 0.1*x**5 -0.2*x**3 + 0.1*x - 0.2
h = 0.05
x = 0.1
#forward differnces approximation
dff1 = (f(x+h) - f(x))/h
dff2 = (f(x +2*h)- 2*f(x+h)+ f(x))/ h**2
print("forwar   d")
print('f\'(%f)= %f' %(x, dff1))
print('f\'\'(%f)= %f' %(x, dff2))

#central differnces approximation
dfc1 = (f(x+h) - f(x-h))/(2*h)
dfc2 = (f(x+h)- 2*f(x)+ f(x-h))/ h**2
print('f\'(%f)= %f' %(x, dfc1))
print('f\'\'(%f)= %f' %(x, dfc2))

#backword differnces approximation
dfb1 = (f(x) - f(x-h))/h
dfb2 = (f(x)- 2*f(x-h)+ f(x-2*h))/ h**2
print('f\'(%f)= %f' %(x, dfb1))
print('f\'\'(%f)= %f' %(x, dfb2))
