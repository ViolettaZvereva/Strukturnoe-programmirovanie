import math
y=0
x=2
while x <= 4.1:
    print("при х=",round(x,2))
    y=y+(2**x-2*(x**2)-1)
    print("y=",round(y,3))
    x=x+0.2
