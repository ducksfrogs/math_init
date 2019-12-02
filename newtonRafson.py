x = 100 

for iteration in range(1, 101):
    x_new = x - (2*x**2 -5*x +3)/(4*x -5)
    if abs(x_new - x) < 0.001:
        break
    x = x_new

print("The root : %0.5f" % x_new)
print("The number of iteration : %d" % iteration)
