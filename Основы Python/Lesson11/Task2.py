class DivZero(Exception):
    def __init__(self, df):
        self.df = df

    def __str__(self):
        return self.df


a = 5
b = 0
try:
    if b == 0:
        raise DivZero('Ошибка: деление на ноль')
    print(a / b)
except DivZero as er:
    print(er)
    exit()
print('done')
