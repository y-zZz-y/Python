# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open('test.txt', 'w') as f:
    while True:
        _ = input('Введите строку (выход - пустая строка)')
        if _:
            f.write(_+'\n')
        else:
            break