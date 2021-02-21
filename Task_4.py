class Car:
    # atributes
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # methods
    def go(self):
        return f'{self.name} Поехала'

    def stop(self):
        return f'{self.name} Остановилась'

    def turn_right(self):
        return f'{self.name} Повернула направо'

    def turn_left(self):
        return f'{self.name} Повернула налево'

    def show_speed(self):
        return f'Текущая скорость {self.name} - {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость town car {self.name} - {self.speed}')

        if self.speed > 40:
            return f'Скорость {self.name} превышена для town car'
        else:
            return f'Скорость {self.name} нормальная для town car'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость work car {self.name} - {self.speed}')

        if self.speed > 60:
            return f'Скорость {self.name} превышена'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} из полиции'
        else:
            return f'{self.name} не из полиции'


audi = SportCar(200, 'Красная', 'Audi', False)
oka = TownCar(20, 'Белая', 'Oka', False)
lada = WorkCar(90, 'Розовая', 'Lada', True)
ford = PoliceCar(300, 'Голубая',  'Ford', True)
print(lada.turn_left())
print(f'Когда {oka.turn_right()}, тогда {audi.stop()}')
print(f'{lada.go()} со скоростью {lada.show_speed()}')
print(f'{lada.name} - {lada.color}')
print(f'Is {audi.name} полицейская? {audi.is_police}')
print(f'Is {lada.name}  полицейская? {lada.is_police}')
print(audi.show_speed())
print(oka.show_speed())
print(ford.police())
print(ford.show_speed())