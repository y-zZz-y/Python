# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
#
# Примечание: длина списка не фиксирована.
# Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
# При этом скрипт завершается, сформированный список выводится на экран.
#
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
# только если введено число.
#
# Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
# При этом работа скрипта не должна завершаться.

class MyException(Exception):
    def __init__(self, err):
        self.err = err

def is_numbers(my):
    for el in my:
        if not el.isdigit():
            raise MyException(f'{el} is not a number!')
    return int(my)


my_list = []

while True:
    my_str = input('Enter a list of numbers (enter q for stop): ')
    if my_str.lower() == 'q':
        break
    try:
        my_list.append(is_numbers(my_str))
    except Exception as err:
        print(type(err), err)

print(my_list)