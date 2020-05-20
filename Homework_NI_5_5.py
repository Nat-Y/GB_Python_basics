# Задание 5

f = open('5_5.txt', 'w')
while True:
    s = input()
    if s == '':
        break
    f.write(s+'\n')
f.close()
t_sum = 0
with open("5_5.txt", "r") as f:
    for line in f:
        a = line.strip().split()
        t_sum += sum(map(int, a))
print(t_sum)