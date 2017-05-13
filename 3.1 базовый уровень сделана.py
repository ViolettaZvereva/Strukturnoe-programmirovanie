A= float (input ("введите вещественное число A= "))
N= int (input ("ведите целое число N>0= "))
i=float
B=1
if (N>0):
    for i in range (N):
        B=B*A
    print (B)
else:
    print ("вы ввели N<0")
    input ()
