print('*'*10, 'Задание 1', '*'*10, end='\n\n')

name = input('Введите Ваше имя: ').upper()
age = input('Введите год Вашего рождения: ')
ageLen = len(age)
ageAsInt = int(age)

while True:

    if ageLen == 4:
        print(name, 'Ваш возраст', 2020-int(age), end='\n\n')
        break

    elif ageLen == 2:
        if int(age) > 20:
            print(name, 'Ваш возраст', 2020 - (int(age)+1900), end='\n\n')
        else:
            print(name, 'Ваш возраст', 20 - int(age), end='\n\n')
        break

    else:
        age = input('Введите год в формате ГГГГ или ГГ: ')
        ageLen = len(age)
        ageAsInt = int(age)