import math
a= float (input ("введите катет a="))
c= float (input("введите гипотенузу c="))
b=math.sqrt((c**2)-(a**2))
S=(1/2)*a*b
print ("второй катет b=", b)
print ("площадь=",S)
