# задание 1

f = open('123.txt', 'w')
while True:
    s = input()
    if s == '':
        break
    f.write(s+'\n')
f.close()
