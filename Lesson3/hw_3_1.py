# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_func(a, b):
    """

    :param a: числитель
    :param b: знаменатель
    :return: возвращаем результат деления, если знаменатель 0 - возвращаем "Ошибка: Деление на ноль!"
    """

    if b == 0:
        return "Ошибка: Деление на ноль!"
    else:
        return a/b

a = int(input("Введите значение числителя: "))
b = int(input("Введите значение знаменателя: "))

print(my_func(a, b))