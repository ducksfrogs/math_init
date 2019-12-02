# 2x**2 -5x + 3 =0
# by bisection method

x1 = 0
x2 = 1

y1 = 2*x1**2 -5*x1 +3
y2 = 2*x2**2 -5*x2 +3

if y1*y2 > 0:
    print("the root is not within the given interval")
    exit
for bisection in range(1,101): #100 bisection
    xh = (x1 + x2)/2
    yh = 2*xh**2 -5*xh +3
    y1 = 2*x1**2 -5*x1 +3

    if abs(y1) < 1.0E-6:
        break
    elif y1 * yh < 0:
        x2 = xh
    else:
        x1 = xh
print("The root : %0.5f" % x1)
print("The number of bisections : %d" % bisection)
