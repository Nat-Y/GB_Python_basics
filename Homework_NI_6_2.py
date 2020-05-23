# Задание 2

class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self):
        height = int(input('input height'))
        mass = int(input('input 1sm asphalt/ sqm mass'))
        return self._length * self._width * height * mass


r = Road(int(input("Введите длину покрытия")), int(input("Введите ширину покрытия")))
print(r.mass())
