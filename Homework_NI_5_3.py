# Задание 3

total_sum = 0
count = 0
ppl = []
with open("5_3.txt", "r") as f:
    for line in f:
        salary = line.split(' ')
        if float(salary[1]) <= 20000:
            ppl.append(salary[0])
        total_sum += float(salary[1])
        count += 1
result = total_sum / count
print(f"ЗП меньше 20к: {ppl}")
print(f"Среднее: {result}")
