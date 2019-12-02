from math import sin, cos
x = 2 #initial guess

for iteration in range(1, 101):

    x_new = x - (x**2 + cos(x)**2 - 4*x)/(2*(x - cos(x)*sin(x) - 2))
    print(iteration, x)
    if abs(x_new - x) < 0.00001:
        break
    x = x_new

print("The iteration %0.5f" % x_new)
print("the number of iteration : %d" % iteration)
