# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.

# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
#
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
#
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

cont = True
summ = 0

def my_func(ml):
    global cont
    summ = 0
    ml = ml.split()
    for n in ml:
        if n == 'Q':
            cont = False
            return summ
        else:
            try:
                _ = int(n)
                summ += _
            except:
                print(f'{n} - не число!')

    else:
        return summ

while cont:
    my_string = input('Введите строку чисел, разделенных пробелом, для завершения работы введите Q: ')
    summ += my_func(my_string)
    print(f'Сумма чисел = {summ}')
