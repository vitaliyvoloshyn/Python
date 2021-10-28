class Road:
    __specific_weight = 25  # расход асфальта при укладке 1 м2 толщиной 1 см

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_mass_asphalt(self, thickness=0):
        """Расчет массы алфальта для укладки
            thickness - толщина слоя в см"""
        total_weight = self._length * self._width * self.__specific_weight * thickness
        print(str(total_weight / 1000) + ' т')


calc = Road(3000, 12)
calc.calc_mass_asphalt(3)
