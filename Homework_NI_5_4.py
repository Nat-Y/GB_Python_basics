# Задание 4

convert = {'One': 'один', 'Two': 'два', 'Three': 'три', 'Four': 'четыре'}
new_file = []
with open('5_4.txt', 'r') as f1:
    for i in f1:
        i = i.split(' ', 1)
        new_file.append(convert[i[0]] + '  ' + i[1])
    print(new_file)

with open('5_4_new.txt', 'w') as f:
    f.writelines(new_file)