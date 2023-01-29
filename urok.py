import math


class Auto:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def move(self, dist):
        self.x += dist * math.cos(self.direction)
        self.y += dist * math.sin(self.direction)

    def set_direction(self, new_direction):
        self.direction = new_direction


class Bus(Auto):
    def __init__(self, x, y, direction):
        super().__init__(x, y, direction)

        self.passengers = 0
        self.money = 0

    def enter_passengers(self, new_passengers):
        self.passengers += new_passengers

    def exit_passengers(self, exit_passengers):
        self.passengers -= exit_passengers

        # self.money +=

    def move(self, dist):
        super().move(dist)
        self.money += self.passengers * dist * 10


def get_direction():
    direction = int(input("""Выберите направление движения
    1: на север
    2: на запад
    3: на юг
    4: на восток\n"""))
    if direction == 1:
        d = math.radians(90)
    elif direction == 2:
        d = math.radians(180)
    elif direction == 3:
        d = math.radians(270)
    elif direction == 4:
        d = math.radians(0)
    return d


bus = Bus(0, 0, get_direction())
while True:
    print("Остановка!")
    if bus.passengers > 0:
        bus.exit_passengers(int(input("Сколько вышло?")))
    bus.enter_passengers(int(input("Сколько вошло?")))
    bus.move(int(input("Сколько проехали?")))
    print(bus.money, round(bus.x), round(bus.y))
    bus.direction = get_direction()
