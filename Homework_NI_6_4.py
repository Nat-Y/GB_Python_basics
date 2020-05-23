# Задание 4


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} is running'

    def stop(self):
        return f'{self.name} is stopped'

    def turn_right(self):
        return f'{self.name} is turning right'

    def turn_left(self):
        return f'{self.name} is turning left'

    def show_speed(self):
        return f'Current speed of {self.name} is {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of town car {self.name} is {self.speed}')

        if self.speed > 40:
            return f'Speed of {self.name} is higher than allowed for town car'
        else:
            return f'Speed of {self.name} is ok for town car'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of work car {self.name} is {self.speed}')

        if self.speed > 60:
            return f'Speed of {self.name} is higher than allowed for work car'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} is from police department'
        else:
            return f'{self.name} is not from police department'


lamba = SportCar(150, 'Yellow', 'Lamba', False)
nissan = TownCar(20, 'Black', 'Nissan', False)
skoda = WorkCar(80, 'White', 'Skoda', True)
patriot = PoliceCar(100, 'Blue', 'Patriot', True)
print(skoda.turn_right())
print(f'When {nissan.turn_left()}, then {lamba.stop()}')
print(patriot.police())
print(patriot.show_speed())
print(f'{skoda.go()} with speed as described: {skoda.show_speed()}')
print(f'{skoda.name} is {skoda.color}')
print(f'Is {lamba.name} a police car? {lamba.is_police}')
print(f'Is {skoda.name}  a police car? {skoda.is_police}')
print(lamba.show_speed())
print(nissan.show_speed())
