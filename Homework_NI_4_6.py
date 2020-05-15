# Задание 6

from itertools import count, cycle

numb = int(input('введите число'))

for el in count(numb):
    if el > (numb + 21):
        break
    else:
        print(el)


с = 0
for el in cycle("da"):
    if с > 5:
        break
    print(el)
    с += 1
