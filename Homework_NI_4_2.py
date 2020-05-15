# Задание 2
import random

my_list = random.sample(range(150), 9)
print(f"Исходный список: {my_list}")
answer = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(f"Новый список: {answer}")

