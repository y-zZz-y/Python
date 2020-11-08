# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.


userTime = int(input('Введите время в секундах: '))

userTimeHours = userTime//3600
userTimeMinutes = (userTime - (userTime//3600)*3600)//60
userTimeSeconds = userTime - userTimeHours*3600 - userTimeMinutes*60


userTimeLine = '{0:02d}:{1:02d}:{2:02d}'.format(userTimeHours, userTimeMinutes, userTimeSeconds)

print(userTime, 'в формате чч:мм:cc', userTimeLine)