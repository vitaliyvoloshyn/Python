from itertools import zip_longest


class Matrix:
    def __init__(self, lst):
        self.lst = lst

    def __str__(self):
        for i in self.lst:
            for y in i:
                print(str(y), end=' ')
            print()
        return ''

    def __add__(self, other):
        temp1 = []  # параметр для будущего обьекта класса Matrix - результат сложения обьектов класса Matrix
        # чтоб осуществить сложение матриц разного размера нужно привести их к одному размеру
        temp2 = self.lst[::]  # вводим доп. список - копию self-списка
        temp2.extend(other.lst)  # расширяем other-списком

        # определяем макс длинну ряда в слаживаемых матрицах
        max_len = len(max(temp2, key=lambda k: len(k)))

        # запускаем процес складывания матриц с помощью zip_longest, поставляя нулевые списки и значения, чтоб выровнять размеры матриц
        for i in zip_longest(self.lst, other.lst, fillvalue=[0 for n in range(max_len)]):
            temp = []
            for y in zip_longest(i[0], i[1], fillvalue=0):
                temp.append(sum(y))
            temp1.append(temp)
        return Matrix(temp1)


v = Matrix([[1, 2], [4, 5], [7, 8], [5, 5]])
print(v)

b = Matrix([[9, 8, 7, 1], [6, 5, 4, 1], [1, 8, 6, 4]])
print(b)

f = v + b
print(f)
