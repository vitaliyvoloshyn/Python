"""
Задание
Дан список, содержащий искажённые данные с должностями и именами сотрудников:
['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

Известно, что имя сотрудника всегда в конце строки. Сформировать и вывести на экран фразы вида: 'Привет, Игорь!'
Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду.
Можно ли при этом не создавать новый список?
"""

# обхожу список в цикле for
# каждый елемент списка (строку) преобразовываю в список с помощью метода split и извлекаю последний элемент (имя),
# попутно приводя к нужному виду с помощью метода title
# вывожу приветствие с помощью f-строки

my_list = ['инженер-конструктов Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
print(my_list)
name = ''
for i in my_list:
    name = list(i.split(' '))[-1].title()
    print(f'Привет, {name}!')
