# task 5
my_list = [7, 5, 3, 3, 2]
add = int(input('Введите натуральное число:'))
ch_add = add in my_list
if ch_add is True:
    pos_new = my_list.index(add)
    pos_q = my_list.count(add)
    pos_add = pos_new + pos_q
else:
    e = 0
    for o in range(len(my_list)):
        if my_list[o] - add < 0:
            break
        e += 1
    pos_add = e
my_list.insert(pos_add, add)
print(my_list)
