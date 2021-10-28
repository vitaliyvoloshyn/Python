class Сlothes:
    def tissue_consumption(self):
        pass


class Coat(Сlothes):
    def __init__(self, size):
        self.__size = size

    def tissue_consumption(self):
        return (f'{self.__size / 6.5 + 0.5:.03}')

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value


class Costume(Сlothes):
    def __init__(self, height):
        self.__height = height

    def tissue_consumption(self):
        return (f'{self.__height * 2 + 0.3:.03}')

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value


jac = Coat(5)
print(f'Размер пальто - {jac.size}')
print(f'Расход ткани на пальто - {jac.tissue_consumption()}')
jac.size = 10
print(f'Размер пальто - {jac.size}')
print(f'Расход ткани на пальто - {jac.tissue_consumption()}')

hac = Costume(5)
print(f'Рост костюма - {hac.height}')
print(f'Расход ткани на пальто - {hac.tissue_consumption()}')
hac.height = 10
print(f'Размер пальто - {hac.height}')
print(f'Расход ткани на пальто - {hac.tissue_consumption()}')
