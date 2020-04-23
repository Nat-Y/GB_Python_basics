# Задание 1
# строки str
new_str = 'Task 1'
upd_new_str = input('Введите Ваше имя: ')
print(new_str, upd_new_str)
# Целое число int
new_int = 198
upd_new_int = int(input('Введите целое число: '))
print(new_int, upd_new_int)

# Дробное число float
new_fl: float = 12.85
upd_new_fl = float(input('Введите дроброе число: '))
print(new_fl, upd_new_fl)

# Булевые значения bool
new_bool = False
print(new_bool)

nmb_mnths = int(input('Введите ваш возраст в месяцах: '))
nmb_yr = int(input('Введите ваш возраст в годах: '))
your_name = input('Введите ваше имя: ')
your_last_name = input('Введите вашу фамилию: ')
print('Ваш возраст', nmb_mnths // 12,'года, вы думаете что вам', nmb_yr, ', Вас зовут', your_name, your_last_name)

#  Задание 2
time_quest = int(input('Введите количество секунд: '))
hr_q = '{:0>2}'.format(time_quest // (3600))
mnt_q = '{:0>2}'.format((time_quest - (int(hr_q) * 3600)) // 60)
sec_q = '{:0>2}'.format(time_quest % 60)
print(f"{hr_q}:{mnt_q}:{sec_q}")

# Задание 3
nmb_n = input('Введите произвольное число: ')
nn = int(nmb_n + nmb_n)
nnn = int(nmb_n + nmb_n + nmb_n)
total = int(nmb_n) + int(nn) + int(nnn)
print(total)

# Задание 4
n_4 = int(input('Введите произвольное число: '))
max_n = n_4 % 10
n_4 = n_4 // 10
while n_4 > 0:
    if n_4 % 10 > max_n:
        max_n = n_4 % 10
    n_4 = n_4 // 10
print(max_n)

# Задание 5
inc_5 = int(input('Пожалуйста введите выручку компании: '))
exp_5 = int(input('Пожалуйста введите издержки компании: '))
prof_5 = inc_5 - exp_5
if prof_5 > 0 :
    print('Вы работаете с прибылью')
    ppl_5 = int(input('Пожалуйста введите количество сотрудников: '))
    print ("Прибыль на сотрудника", prof_5 / ppl_5)
else: print('Вы работаете в убыток')

# Задание 6

dist_6 = int(input('Пожалуйста введите дистанцию бега в первый день: '))
dist_6_upd = int(input('Пожалуйста введите требуемую дистанцию бега: '))
day_nmb = 1
while dist_6 < dist_6_upd:
    day_nmb = day_nmb + 1
    dist_6 = dist_6 * 1.1
print('На', day_nmb, 'день бегун сможет бежать не менее', dist_6_upd,'км')
