from time import sleep

class TrafficLight:

    def trafficlight_on(self):
        print(f'Светофор включен: \n')
        print("Красный цвет")
        sleep(7)
        print("Желтый цвет")
        sleep(2)
        print("Зеленый цвет")
        sleep(10)

tc = TrafficLight()
tc.trafficlight_on()

#-----------------------------------------

class road:

    def road_mass(self, length, width):
        self._mass = (length * width * 25 * 5) / 1000

r = road()
r.road_mass(int(input("Введите длину полотна: ")), int(input("Введите ширину полотна: ")))
print(f"{r._mass}, Т")

#-----------------------------------------

class Worker:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.position = "Инженер "
        self._income = {"Оклад": 30000, "Премия":25000}

class Position(Worker):

    def __init__(self, name, surname):
        super().__init__(name, surname)

    def get_full_name(self):
        return self.name + self.surname

    def get_total_income(self):
        return self.position

p = Position("Илья ", "Новиков ")
print(p.get_full_name())
print(p.get_total_income())

#-----------------------------------------------

from time import sleep
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print("Машина повернула на: ", direction)

    def show_speed(self):
        print("Скорость авто: ")

class Towncar(Car):
    def __init__(self, speed, color, name, is_police):
         super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f'Машина {self.name} превысила скорость')
        else:
            print(f'Скорость авто: {self.speed}')

class Workcar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f'Машина {self.name} превысила скорость')
        else:
            print(f'Скорость авто: {self.speed}')

c = Workcar(70, "Зеленый", "Мазда", False)
c.go()
sleep(5)
c.turn("Налево")
c.show_speed()

#------------------------------------------------------------

class Stationery:
    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def draw(self):
        print("Отрисовка выполнена ручкой")

class Pencil(Stationery):
    def draw(self):
        print("Отрисовка выполнена карандашом")

class Handle(Stationery):
    def draw(self):
        print("Отрисовка выполнена маркером")

s = Stationery()
s.draw()
s = Pencil()
s.draw()
