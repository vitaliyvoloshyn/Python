from time import sleep


class TrafficLight():
    __color = 'красный'

    def running(self):
        print(self.__color)
        sleep(7)
        self.__color = 'жёлтый'
        print(self.__color)
        sleep(2)
        self.__color = 'зеленый'
        print(self.__color)
        sleep(7)


a = TrafficLight()
a.running()
