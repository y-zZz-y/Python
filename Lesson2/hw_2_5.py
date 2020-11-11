# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением"'{0}'".format(n) for n in numbers
# должен разместиться после них.
#
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
#
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
#
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
#
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
#
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

myList = [7, 5, 3, 3, 2]
myListReverse = list(myList)
myListReverse.reverse()

print(f'Набор натуральных чисел: {", ".join("{0}".format(n) for n in myList)}')


myNumber = int(input('Введите новый элемент рейтинга: '))

myCount = myListReverse.count(myNumber)

if myCount > 0:
    myListReverse.insert(myListReverse.index(myNumber), myNumber)
    myList = list(myListReverse)
    myList.reverse()

else:
    for n in myList:
        if n < myNumber:
            myList.insert(myList.index(n), myNumber)
            break
    else:
        myList.append(myNumber)

print(f'Результат: {", ".join("{0}".format(n) for n in myList)}')

