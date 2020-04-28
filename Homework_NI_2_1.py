#task 1

my_list = ['Age', 34, 37.3, False, [1,2,3,12]]
print(type(my_list))
for n in range(len(my_list)):
    print(type(my_list[n]))

# так как задание 1 слишком короткое добавила немного вариантов решения задач
my_list = ['Зима', 12, 1, 2, 'Весна', 3, 4, 5, 'Лето', 6, 7, 8, 'Осень', 9, 10, 11]
imon = int(input('Введите номер месяца: '))
i = my_list.index(imon)
if i < 4:
    print('Это', my_list[0])
elif 3 < i < 8:
    print('Это', my_list[4])
elif 7 < i < 12:
    print('Это', my_list[8])
elif 11 < i:
    print('Это', my_list[12])

my_list = ['Зима', 'Весна', 'Лето', 'Осень']
imon = int(input('Введите номер месяца: '))
if imon < 3 and imon == 12:
    print('Это', my_list[0])
elif 2 < imon < 6:
    print('Это', my_list[1])
elif 5 < imon < 9:
    print('Это', my_list[2])
elif 8 < imon < 12:
    print('Это', my_list[3])