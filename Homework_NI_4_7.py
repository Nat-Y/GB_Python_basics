# task 7
from math import factorial


def fact(x):
    for i in range(1, x+1):
        yield factorial(i)


n = int(input("Введите число для вычисления факториала"))
for el in fact(n):
    print(el)
