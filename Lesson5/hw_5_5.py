# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('hw_5_5.txt','w') as f:
    f.write(input('Введите числа через пробел: '))

with open('hw_5_5.txt','r') as f:
    print(f'Сумма чисел: {sum(map(int,f.readline().split()))}')