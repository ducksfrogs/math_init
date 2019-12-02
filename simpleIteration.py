import math

x = 0 #initial guess

for iteration in range(1, 101):
    x_new =  (2*x**2 + 3) / 5
    print(iteration, x)
    if abs(x_new - x) < 0.00001:
        break
    x = x_new

print("The iteration %0.5f" % x_new)
print("the number of iteration : %d" % iteration)
