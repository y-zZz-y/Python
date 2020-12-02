# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.
#
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
#
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

from abc import abstractmethod, ABC

class Warehouse:

    def __init__(self, name):
        self.name = name
        self.cnt_eq = []

    def __str__(self):
        return f'In warehouse {self.name}: {[f"{el.name} {el.title}" for el in self.cnt_eq]}'

class OfficeEquipment(ABC):
    __where = 0

    def __init__(self, name, title):
        self.name = name
        self.title = title

    def __str__(self):
        return f'Office equipment name: {self.name}'

    def get_where(self):
        return self.__where.name

    def put_in(self, other):
        if self.__where:
            self.__where.cnt_eq.remove(self)
        self.__where = other
        other.cnt_eq.append(self)
        return other.name

    @abstractmethod
    def main_action(self):
        pass

class Printer(OfficeEquipment):

    def __init__(self, name, title):
        super().__init__(name, title)

    def main_action(self):
        return 'Print documents'

class Scaner(OfficeEquipment):
    def __init__(self, name, title):
        super().__init__(name, title)

    def main_action(self):
        return 'Scan documents'

class Xerox(OfficeEquipment):
    def __init__(self, name, title):
        super().__init__(name, title)

    def main_action(self):
        return 'Copy documents'

main_warehouse = Warehouse('Main')
depart_warehouse = Warehouse('Depart')

scaner = Scaner('Scaner','Epson')
printer = Printer('Printer','HP')

scaner.put_in(main_warehouse)
printer.put_in(depart_warehouse)
print(scaner.get_where())
print(printer.get_where())
print(main_warehouse)
print(depart_warehouse)

scaner.put_in(depart_warehouse)
print(scaner.get_where())
print(depart_warehouse)
print(main_warehouse)

scaner.put_in(main_warehouse)
print(depart_warehouse)
print(main_warehouse)