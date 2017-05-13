import math
n=int(input ("Введите число n-"))
q=0
v=0
for k in range(1,n+1):
    print("при k=",k)
    print("при n=",n)
    t=(-1**k)*(k-7)
    u=2*math.factorial(n-k)
    if u==0:
        k=k+1
    else:
        q=q+(t/u)
        v=v+1
        print("Действте",v,"сумма=",round(q,3))

