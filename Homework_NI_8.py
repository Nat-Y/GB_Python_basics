import random
import sys


ballstotal = 90
numtotal = 15
p1 = numtotal
p2 = numtotal
balls = random.sample(range(1, 91), 90)
game_set = random.sample(range(1, 91), (numtotal*2))
p1_set = random.sample(game_set, numtotal)
p2_set = [e for e in game_set if not e in p1_set]
p1_field = [p1_set[:5], p1_set[5:10], p1_set[10:]]
p2_field = [p2_set[:5], p2_set[5:10], p2_set[10:]]
for p1line in p1_field:
    p1line.sort()
    p1line.insert(random.randint(0, 4), ' ')
    p1line.insert(random.randint(0, 5), ' ')
    p1line.insert(random.randint(0, 6), ' ')
    p1line.insert(random.randint(0, 7), ' ')
for p2line in p2_field:
    p2line.sort()
    p2line.insert(random.randint(0, 4), ' ')
    p2line.insert(random.randint(0, 5), ' ')
    p2line.insert(random.randint(0, 6), ' ')
    p2line.insert(random.randint(0, 7), ' ')


# Actions

def field(p):
    if p == 0:
        print('{:*^26}'.format(' Your Card '))
        for line1 in p1_field:
            for n1 in line1:
                print('{0:>2}'.format(n1), end=' ')
            print()
        print('{:*^26}\n'.format('*'))
    if p == 1:
        print('{:*^26}'.format(' PC Card '))
        for line2 in p2_field:
            for n2 in line2:
                print('{0:>2}'.format(n2), end=' ')
            print()
        print('{:*^26}\n'.format('*'))


def your_move():

    while True:
        a = input('Зачеркнуть цифру? (y/n):')
        if a == 'y':
            if ball in p1_set:
                for el in p1_field:
                    try:
                        el.insert(el.index(ball), '><')
                        el.pop(el.index(ball))
                    except ValueError:
                        continue
                print('\nOK')
                break
            else:
                print('\nGAME OVER')
                sys.exit()
        if a == 'n':
            if ball in p1_set:
                print('\nGAME OVER')
                sys.exit()
            else:
                print('\nOK')
                break
        if ValueError:
            print('Enter y or n')


def pc_move():
    if ball in p2_set:
        for i in p2_field:
            try:
                i.insert(i.index(ball), '><')
                i.pop(i.index(ball))
            except ValueError:
                continue

for ball in balls:
    ballstotal -= 1
    print('\nНовый номер: {} (осталось номеров: {})\n'.format(ball, ballstotal))
    field(0)
    field(1)
    if your_move() == 1:
        p1 -= 1
    if pc_move() == 1:
        p2 -= 1
    if p1 == 0:
        print('\nYOU WON')
        sys.exit()
    if p2 == 0:
        print('\nYOU LOSE')
        sys.exit()
    if ballstotal == 0:
        print('\nGAME OVER')
        sys.exit()
