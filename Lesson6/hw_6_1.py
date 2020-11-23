# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.

# Продолжительность первого состояния
# (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение.

# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
#
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.
#
from time import sleep
from itertools import cycle, count

class TrafficLight:
    __color = 'red'

    def __init__(self, color=__color):
        self.color = color

    def running(self, red=10, yellow=3, green=10, cnt=5):
        cnt = cnt * 3
        color = ('red','yellow','green')
        for el in cycle(color):
            if cnt:
                self.color = el
                print(el)
                if el == 'red':
                    sleep(red)
                elif el == 'yellow':
                    sleep(yellow)
                else:
                    sleep(green)
                cnt -= 1
            else:
                break

traffic_light = TrafficLight()
traffic_light.running(7,2,5,2)