N = 10
array = []
print("Введите целые числа")

for i in range(N):
    N = int(input())
    array.append(N)

max = array[0]
pos = 0
for i in range(len(array)):
    if array[i]>max:
        max=array[i];
        pos=i
        
print (array)
print("max=",max,", pos=",pos , " - отсчет начинается с нуля")

min=array[0]
imax=array.index(max)
imin=array.index(min)
array[imin], array[imax] = array[imax], array[imin]
print (array)





