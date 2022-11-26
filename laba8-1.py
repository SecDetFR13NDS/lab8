import statistics
import math
n = []
m = int(input("Введіть розмір масиву:  "))
print("Введіть елементи масиву: ")
n = list(map(int, input().split()))
print("Масив: ")
print(n)
print("Середнє арифметичне: ")
print(str(statistics.mean(n)))
