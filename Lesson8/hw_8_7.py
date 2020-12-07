# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел.
#
# Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров.
#
# Проверьте корректность полученного результата.

class Complex:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def __str__(self):
        if self.__a == 0:
            return f'{self.__b}i'
        elif self.__b == 0:
            return f'{self.__a}'
        else:
            return f'{self.__a}+{self.__b}i'

    def __add__(self, other):
        return Complex(self.__a + other.__a, self.__b + other.__b)

    def __sub__(self, other):
        return Complex(self.__a - other.__a, self.__b - other.__b)

    def __mul__(self, other):
        return Complex((self.__a * other.__a) - (self.__b * other.__b), (self.__b * other.__a) + (self.__a * other.__b))

    def __truediv__(self, other):
        return Complex(((self.__a * other.__a)+(self.__b * other.__b)) / ((other.__a * other.__a) + (other.__b * other.__b)), ((self.__b * other.__a) - (self.__a * other.__b))/((other.__a * other.__a)+(other.__b * other.__b)))


com = Complex(2, 4)
com1 = Complex(0, 3)
com2 = Complex(5, 0)

print(com)
print(com1)
print(com2)

print(com+com1)
print(com-com1)
print(com*com1)
print(com/com1)