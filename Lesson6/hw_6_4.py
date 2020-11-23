# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
#
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    __is_polis = False
    __is_go = False
    __is_stop = True

    def __init__(self, speed, color, name, is_police=__is_polis):
        self.speed = speed
        if speed > 0:
            self.__is_go = True
            __is_stop = False

        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        if self.__is_go:
            return f'The {self.name} speed is {self.speed}'
        else:
            return f'The {self.name} stopped!'

    def go(self):
        self.__is_go = True
        self.__is_stop = False
        return f'The {self.name} started to go'

    def stop(self):
        self.__is_stop = True
        self.__is_go = False
        return f'The {self.name} stopped'

    def turn(self, direction):
        return f'The {self.name} turn to the {direction}'

class TownCar(Car):
    _speed_limit = 60

    def show_speed(self):
        if self.speed > self._speed_limit:
            return f'The {self.name} speed is exceeded by {self.speed - self._speed_limit}'
        else:
            return f'The {self.name} speed is {self.speed}'

class SportCar(Car):
    pass

class WorkCar(Car):
    _speed_limit = 40

    def show_speed(self):
        if self.speed > self._speed_limit:
            return f'The {self.name} speed is exceeded by {self.speed - self._speed_limit}'
        else:
            return f'The {self.name} speed is {self.speed}'

class PoliceCar(Car):
    __is_polis = True
    __lights_on = False

    def lights(self, on=False):
        __lights_on = on
        if __lights_on:
            return f'The {self.name} lights is ON'
        else:
            return f'The {self.name} lights is OFF'

town_car = TownCar(90, 'white', 'Town car')
print(town_car.go())
print(town_car.show_speed())
print(town_car.turn('Left'))
print(town_car.stop())

sport_car = SportCar(190, 'red', 'Ferrari')
print(f'Sport car {sport_car.name}: color {sport_car.color}')
print(sport_car.go())
print(sport_car.show_speed())
print(sport_car.turn('Right'))
print(sport_car.stop())

work_car = WorkCar(90,'black','Work car')
print(work_car.go())
print(work_car.show_speed())
print(work_car.turn('Left'))
print(work_car.stop())

police_car = PoliceCar(290,'blue','Police car')
print(police_car.lights(True))
print(police_car.go())
print(police_car.show_speed())

police_car.speed = 50

print(police_car.show_speed())
print(police_car.turn('Right'))
print(police_car.stop())
print(police_car.lights())