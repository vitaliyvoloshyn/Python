class IsNum(Exception):
    def __str__(self):
        return 'Веденное значение не является целым числом'


lst = []
a = ''
while a != 'stop':
    a = input('Введите целое число: ')
    try:
        if not a.isdigit():
            raise IsNum
        else:
            lst.append(int(a))
    except IsNum as er:
        print(er)
print(lst)
