"""
Задание
Дан список:
['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками
(добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных
разрядов:
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']

Сформировать из обработанного списка строку:
в "05" часов "17" минут температура воздуха была "+05" градусов

Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие
для чисел со знаком?
"""


my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
update_list = []


# проходим циклом по списку, находим числа, форматируем их и вставляем кавычки
n = 1  # счетчик нахождения чисел, нужен, чтоб третье число форматировать со знаком "+"
for i in my_list:
    if i.isalpha():
        update_list.append(i)
    else:
        update_list.append('"')
        update_list.append(f'{int(i):02}')
        if n == 3:
            update_list[-1] = f'{update_list[-1]:+>3}'
        update_list.append('"')
        n += 1
print(update_list)

# собираем итоговую строку
result_str = ""
n = 1
# проходим циклом по новому списку, добавляя в строку по одному элементу списка кроме "
# до и перед числом вставляем "
for i, value in enumerate(update_list):
    if not value.isalpha() and value != '"':
        if i == 0:
            result_str += value + '"'
        elif i == len(update_list) - 1:
            result_str += '"' + value + ' '
        else:
            result_str += '"' + value + '" '
        n += 1
    elif value.isalpha():
        if i == len(update_list) - 1:
            result_str += value
        else:
            result_str += value + ' '

print(result_str)
