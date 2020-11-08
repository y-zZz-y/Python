#2. Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

print('Введите несколько произвольных элементов списка, для завершения списка наберите "выход"')
myList = list()

while True:
    stop = input("Введите элемент списка: ")
    if stop == 'выход':
        break
    else:
        myList.append(stop)
        print(myList, len(myList))

myListLen = len(myList)-1

for step in range(0,myListLen,2):
    if step < myListLen:
        myList[step], myList[step+1] = myList[step+1], myList[step]
        print(step, myList)
