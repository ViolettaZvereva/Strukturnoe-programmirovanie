import math
x=2.7
t= float (input ("введите переменную t="))
a=math.log10(x)
b=math.sqrt (x**2+t**2)
y= (math.fabs(a-b*x))**(1/5)
print("y=", y)
print("a=" , a)
print("b=", b)
input()
