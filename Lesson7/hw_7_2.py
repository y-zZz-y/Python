# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
#
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
#
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import abstractmethod, ABC
from functools import reduce

class MyClo(ABC):
    __name = 'Clothes'
    def __init__(self, name=__name):
        self.name = name

    @abstractmethod
    def consumption(self):
        pass

    @staticmethod
    def get_consumption(get_list:list):
        return reduce(lambda a,b: a+b, get_list)


class MyCoat(MyClo):
    def __init__(self, name, v=0):
        super().__init__(name)
        self.v = v

    def __str__(self):
        return f'Clothes: {self.name} size {self.v}'

    @property
    def consumption(self):
        return self.v / 6.5 + 0.5

class MyCostume(MyClo):
    def __init__(self, name, h=0):
        super().__init__(name)
        self.h = h

    def __str__(self):
        return f'Clothes: {self.name} height {self.h}'

    @property
    def consumption(self):
        return 2*self.h + 0.3

my_coat = MyCoat('Coat', 1)
my_coat2 =  MyCoat('Coat 2', 2)
print(my_coat)

my_costume = MyCostume('Costume', 6)
my_costume2 = MyCostume('Costume 10', 10)
print(my_costume)

print(f'Tissue consumption: {MyClo.get_consumption([my_coat.consumption,my_coat2.consumption,my_costume.consumption,my_costume2.consumption])}')