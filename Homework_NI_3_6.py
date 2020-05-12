# задание 6


def int_func(func_w):
    cap_word = func_w.title()
    return cap_word


word = input("Input one word ")
print(int_func(word))

my_string = str(input('Введите несколько слов через пробел:'))
my_list = my_string.split()
result = ' '.join(list(map(int_func, my_list)))
print(result)
