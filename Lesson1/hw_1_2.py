print('*'*10, 'Задание 2', '*'*10, end='\n\n')

userTime = int(input('Введите время в секундах: '))

userTimeHours = userTime//3600
userTimeMinutes = (userTime - (userTime//3600)*3600)//60
userTimeSeconds = userTime - userTimeHours*3600 - userTimeMinutes*60

if userTimeHours < 10:
    userTimeHours = '{}{}'.format('0', userTimeHours)
if userTimeMinutes < 10:
    userTimeMinutes = '{}{}'.format('0', userTimeMinutes)
if userTimeSeconds < 10:
    userTimeSeconds = '{}{}'.format('0', userTimeSeconds)

userTimeLine = '{}:{}:{}'.format(userTimeHours, userTimeMinutes, userTimeSeconds)

print(userTime, 'в формате чч:мм:cc', userTimeLine)