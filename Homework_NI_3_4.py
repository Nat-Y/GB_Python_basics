# задание 4


def my_func(x, y):
    step = 1 / (x ** abs(y))
    return step


print(my_func(int(input('input positive number')), int(input('input negative number'))))


def my_func(x, y):
    k = 0
    step = 1
    while k in range(abs(y)):
        step *= 1 / x
        k += 1
    return step


print(my_func(int(input('input positive number')), int(input('input negative number'))))
