print('*'*10, 'Задание 4', '*'*10, end='\n\n')

digit = input('Введите целое положительное число: ')

i = len(digit)-1
max = 0

while i > 0:
    if int(digit[i]) > max:
        max = int(digit[i])
    i-=1

print('Максимальная цифра =', max)