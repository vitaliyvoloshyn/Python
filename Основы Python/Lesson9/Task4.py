class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} go')

    def stop(self):
        print(f'{self.name} stop')

    def turn(self, direction):
        print(f'{self.name} turn {direction}')

    def show_speed(self):
        print(f'{self.speed} km/h')


class TownCar(Car):
    # def __init__(self, speed, color, name, is_police):
    #     super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 60:
            super().show_speed()
            print('Внимание! Превышение скорости')
        else:
            super().show_speed()


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            super().show_speed()
            print('Внимание! Превышение скорости')
        else:
            super().show_speed()


class PoliceCar(Car):
    pass


toyota = TownCar(61, 'white', 'toyota', True)
print(toyota.__dict__)
toyota.go()
toyota.stop()
toyota.turn('right')
toyota.show_speed()
