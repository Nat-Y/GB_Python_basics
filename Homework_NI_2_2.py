#task 2

n_list = int(input('введите количество элементов списка: '))
my_list = []
i = 0
for i in range(n_list):
    print ('Введите элемент на', i, 'месте списка')
    my_list.append(input(str()))
print('Было', my_list)
i = 0
for i in range(n_list - 1):
    if i % 2 == 0:
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print('Стало', my_list)