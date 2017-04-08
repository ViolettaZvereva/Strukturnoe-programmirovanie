import math
a= float (input ("введите сторону а ="))
b=float (input ("введите сторону b="))
c=float (input ("введите сторону c="))
if (a**2+b**2==c**2) or (b**2+c**2==a**2) or (c**2+a**2==b**2):
    print ("прямоугольный треугольник")
else:
    print ("треугольник не прямоугольный")
input ()

