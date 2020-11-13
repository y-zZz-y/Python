# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func(a, b, c):
    my_list = sorted((a, b, c), reverse=True)
    return my_list[0]+my_list[1]

print(my_func(15,20,85))
