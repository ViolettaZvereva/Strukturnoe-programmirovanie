n=int(input ("ведите число n-"))
s=0
for i in range(n+1):
    print(i,' ')
    if i%2==0:
        s=s+(i**2)
    else:
        s=s+(i**3)
print('сумма квадратов чётных и кубов нечётных-',s)

