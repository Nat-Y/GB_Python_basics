# Task 4

my_string = str(input('Введите несколько слов через пробел:'))
my_list = my_string.split()
print(my_list)
for my_list, el in enumerate(my_list):
    print(my_list, el[:10])