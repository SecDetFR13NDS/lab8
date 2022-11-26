from random import randint
n = int(input('Кількість рядків: '))
m = int(input('Кількість стовпчиків: '))
A = []
for i in range(n*m):
    A.append(randint(1, 20))
index = 0
sum_n = []
sum_m = []
s = 0
index2 = 0
for i in range(m):
    for j in range(n):
        s += A[index+index2]
        index2 += m
    sum_m.append(s)
    index += 1
    index2 = 0
    s = 0
index = 0
for i in range(n):
    sum_n.append(sum(A[index:index+m]))
    for j in range(m):
        print(A[index], end=' ')
        index += 1
    print()
print('Рядок, сума елементів якого найбільша:', max(sum_n))
print('Стовпчик, сума елементів якого найбільша:', max(sum_m))
