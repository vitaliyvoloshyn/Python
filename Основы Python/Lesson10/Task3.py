class BioCell:

    @staticmethod
    def __cells_validate(value):
        if value <= 0:
            raise ValueError('количество ячеек должно быть больше 0')
        else:
            return True

    def __init__(self, cells):
        if BioCell.__cells_validate(cells):
            self.__cells = cells

    @property
    def cells(self):
        return self.__cells

    @cells.setter
    def cells(self, value):
        if BioCell.__cells_validate(value):
            self.__cells = value

    def __add__(self, other):
        return BioCell(self.__cells + other.__cells)

    def __sub__(self, other):
        if self.__cells > other.__cells:
            return BioCell(self.__cells - other.__cells)
        else:
            raise ValueError('результат вычитания должен быть больше 0')

    def __mul__(self, other):
        return BioCell(self.__cells * other.__cells)

    def __floordiv__(self, other):
        return BioCell(self.__cells // other.__cells)

    def __truediv__(self, other):
        return BioCell(self.__cells / other.__cells)

    def make_order(self, cells_count):
        res = ('*' * cells_count + '\n') * (self.__cells // cells_count)
        res = res + '*' * (self.__cells % cells_count)
        print(res)


c1 = BioCell(7)
print(dir(c1))
c2 = BioCell(9)
c3 = c1 + c2
print(c3.cells)
c3.make_order(7)
