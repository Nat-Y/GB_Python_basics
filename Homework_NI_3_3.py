# задание 3


def my_func(*args):
    numbers = [*args]
    numbers.sort(reverse=True)
    summa = sum(numbers[:2])
    return summa


print(my_func(int(input("number1:")), int(input("number2:")), int(input("number3:"))))
