#4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

myString = input("Вводите строку из нескольких слов, разделённых пробелами: ")

myString = myString.split()

for step in myString:

    print(myString.index(step)+1, step[:10])