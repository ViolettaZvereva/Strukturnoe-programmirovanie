N=9
Z=7
a=[0,0,0,0,0,0,0,0,0]
b=[0,0,0,0,0,0,0]
c=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

print ("Введите число")
for i in range (N):
    a[i]=float(input())
print (a)

print ("Введите число")
for i in range (Z):
    b[i]=float (input())
print (b)
print ()
a.sort()
print ("отсортированный массив один", a)
b.sort()
print ("отсортированный массив два", b)

c=sorted (a)+ sorted (b)
c.sort()
print ("отсортированный массив три", c)



    
