# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
#
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
#
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:

    def __init__(self, title=""):
        self.title = title

    def draw(self):
        return "Это канцелярская принадлежность!"

class Pen(Stationery):
    def draw(self):
        return f"Это {self.title}!"
class Pencil(Stationery):
    def draw(self):
        return f"Это {self.title}!"
class Handle(Stationery):
    def draw(self):
        return f"Это {self.title}!"

my_stationery = Stationery()
print(my_stationery.draw())

my_pen = Pen('Ручка')
print(my_pen.draw())

my_pencil = Pencil('Карандаш')
print(my_pencil.draw())

my_handle = Handle('Маркер')
print(my_handle.draw())
