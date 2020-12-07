# 4. Создать (не программно) текстовый файл со следующим содержимым:
#
# One — 1
#
# Two — 2
#
# Three — 3
#
# Four — 4
#
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
#

numbers = ['Один','Два','Три','Четыре']

with open('hw_5_4.txt','w') as f:
    f.write('One — 1\n')
    f.write('Two — 2\n')
    f.write('Three — 3\n')
    f.write('Four — 4\n')

with open('hw_5_4.txt','r') as f:
    for line in f:
        line = line.replace('\n','').split(sep=' — ')
        line[0] = numbers[int(line[1])-1]
        with open('hw_5_4_.txt','a') as _:
            _.write(' — '.join(line)+'\n')