# Задание 2

lines = 0
words = 0
for line in open('123.txt', 'r'):
    lines += 1
    pos = 'end'
    for letter in line:
        if letter != ' ' and pos == 'end':
            words += 1
            pos = 'space'
        elif letter == ' ':
            pos = 'end'
print("Строк:", lines)
print("Слов:", words)
