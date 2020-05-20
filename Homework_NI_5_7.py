# Задание 7

import json
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('5_7.txt', 'r') as f:
    for line in f:
        name, firm, earn, loss = line.split()
        profit[name] = int(earn) - int(loss)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Прибыль средняя - {prof_aver:.2f}')
    else:
        print(f'Все работают в убыток')
    pr = {'средняя прибыль': round(prof_aver)}
    profit1 = [profit,pr]
    print(f'Прибыль - {profit1}')

with open('5_7.json', 'w') as write_js:
    json.dump(profit1, write_js)

    js_str = json.dumps(profit1)
    print(f'Создан файл с расширением json со следующим содержимым: \n '
          f' {js_str}')
