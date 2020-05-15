# задание 1

from sys import argv
Salary_count, h_salary, hours_worked, bonus = argv
print("Имя скрипта: ", Salary_count)
print("Почасовая оплата: ", h_salary)
print("Отработано часов: ", hours_worked)
print("Премия: ", bonus)
print("Зарплата итого", (int(h_salary) * int(hours_worked) + int(bonus)))
