# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
#
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
#
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
#
# Проверить работу полученной структуры на реальных данных.

class MyDate:
    def __init__(self, date_str:str):
        self.date_str = date_str

    @staticmethod
    def validate(number:dict):
        day = number.get("DD")
        month = number.get("MM")
        year = number.get("YYYY")

        if year < 21:
            year += 2000
        elif year < 100:
            year += 1900

        leap = ((year % 4 == 0) and (year % 100 > 0)) or (year % 400 == 0)

        if (day not in range(1,32)):
            return f'Day {day} out of range!'
        elif (month in [4,6,9,11] and day == 31):
            return f'Day {day} out of range!'
        elif (month == 2 and day > 29 and leap) or (month == 2 and day > 28 and not leap):
            return f'Day {day} out of range!'

        if month not in range(1,13):
            return f'Month {month} out of range!'

        return f'Date {day}-{month}-{year} is valid'

    @property
    def date_to_number(self):
        tmp = list(map(int,self.date_str.split(sep='-')))
        return {"DD":tmp[0],"MM":tmp[1],"YYYY":tmp[2]}

my_date = MyDate('12-12-12')

print(my_date.date_to_number)

my_date1 = MyDate('29-02-19') # not valid
print(MyDate.validate(my_date1.date_to_number))