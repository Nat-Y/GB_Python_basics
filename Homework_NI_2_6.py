# Task 6
num_k = int(input('Введите количество позиций которое вы предполагаете ввести: '))
i = 1
final_list = []
name_list = []
price_list = []
qtty_list = []
unit_list = []
while i <= num_k:
    name_g = str(input('Введите название товара: '))
    price_g = int(input('Введите цену товара: '))
    qtty_g = int(input('Введите количество товара: '))
    unit_g = str(input('Введите единицу измерения товара (шт, л, и тд): '))
    kort = (i, {'Название': name_g, 'Цена': price_g, 'Количество': qtty_g, 'Ед изм': unit_g})
    print(kort)
    final_list.append(kort)
    name_list.append(name_g)
    price_list.append(price_g)
    qtty_list.append(qtty_g)
    unit_list.append(unit_g)
    i += 1

dict_f = {'Название': list(set(name_list)),
          'Цена': list(set(price_list)),
          'Количество': list(set(qtty_list)),
          'Ед изм': list(set(unit_list))}
print(final_list)
print(dict_f)
