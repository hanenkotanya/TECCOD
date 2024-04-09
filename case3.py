# Создать класс Point, который представляет собой точку в двумерном пространстве.
# Класс должен иметь методы для инициализации координат точки,
# вычисления расстояния до другой точки, а также для получения и изменения координат.


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other):
        return print(((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5)

    def coord(self):
        return print(f"Координаты данной точки: {self.x}, {self.y}")

    def ism(self):
        self.x = int(
            input(
                f"Сейчас первое значение координат точки {self.x}, введите новое значение "
            )
        )
        self.y = int(
            input(
                f"Сейчас второе значение координат точки {self.y}, введите новое значение "
            )
        )
        return self.x, self.y


point3 = Point(1, 1)
point4 = Point(8, 8)

Point.dist(point3, point4)
Point.coord(point3)
Point.ism(point3)
Point.coord(point3)
