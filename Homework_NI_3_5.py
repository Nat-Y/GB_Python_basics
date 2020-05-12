# Задача 5


def my_func():
    summary_all = 0
    check = False
    while check == False :
        my_numb = input('Введите числа через пробел или q чтобы выйти:').split()
        for el in range(len(my_numb)):
            if my_numb[el] == 'q' or my_numb[el] == 'Q':
                check = True
                break
            summary_all += int(my_numb[el])
        print('Промежуточная сумма', summary_all)
    return summary_all

print('Итоговая сумма', my_func())
