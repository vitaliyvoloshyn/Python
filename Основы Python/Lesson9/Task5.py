class Stationery:
    def __init__(self, title):
        self.title = title
        # print (self.title)

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки - ручка")


class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки - карандаш")


class Marker(Stationery):
    def draw(self):
        print(f"Запуск отрисовки - маркер")


a = Pen('ручка')
a.draw()

b = Pencil('карандаш')
b.draw()

c = Marker('маркер')
c.draw()
