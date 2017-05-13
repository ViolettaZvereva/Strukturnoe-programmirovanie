n = int(input("введите размер матрицы,затем элементы построчно- ")) 
a = []
for i in range(n):
    a.append([int(j) for j in input().split()])
min=a[0][n-1]
for i in range(0,n):
    for j in range(0,n):
        if ((i+j) == (n-1)) and a[i][j] < min:
            min=a[i][j]
print(a)
print("наименьший элемент побочной диагонали - ", min)
