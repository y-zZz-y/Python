# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class MyException(Exception):
    def __init__(self, err):
        self.err = err

def div(a,b):
    if not b:
        raise MyException("Division by zero!")
    return a/b

a = int(input('Input dividend: '))
b = int(input('Input divisor: '))

try:
    div(a,b)
except Exception as err:
    print(type(err), err)