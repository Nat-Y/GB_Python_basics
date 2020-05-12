# Задача 1
def div_calc(arg1, arg2):
    try:
        res = int(arg1) / int(arg2)
    except ValueError:
        return 'Введите числа'
    except ZeroDivisionError:
        return 'Деление на ноль'
    return res


print(div_calc(input("Укажите число которое делим:"), input("Укажите число на которое делим:")))
