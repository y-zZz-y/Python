# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
#
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
#
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
#
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
#
# Пример json-объекта:
#
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.

from functools import reduce
import json

my_list = []
firms = {}
profit = 0

with open('hw_5_7.txt', 'w') as f:
    f.write('firm_1 ООО 10000 5000\nfirm_2 ООО 15000 7000\nfirm_3 ООО 20000 5000')

with open('hw_5_7.txt', 'r') as f:
    for line in f:
        line = line.split()
        _ = reduce(lambda a,b: a-b, map(int,line[2:]))
        firms.update([(line[0], _)])
        profit += _


my_list.append(firms)
my_list.append({"average_profit":profit/len(firms)})

with open("my_list.json", "w") as write_f:
    json.dump(my_list, write_f)