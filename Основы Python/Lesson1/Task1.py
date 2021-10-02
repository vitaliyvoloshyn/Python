# Реализовать вывод информации о промежутке времени в зависимости от его
# продолжительности duration в секундах:
# до минуты: <s> сек;
# до часа: <m> мин <s> сек;
# до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.

# Примеры:
#
# duration = 53
# 53 сек
# duration = 153
# 2 мин 33 сек
# duration = 4153
# 1 час 9 мин 13 сек
# duration = 400153
# 4 дн 15 час 9 мин 13 сек
#
# Примечание: можете проверить себя здесь, подумайте, можно ли использовать цикл для проверки
# работы кода сразу для нескольких значений продолжительности, будет ли тут полезен список?


duration_list = []
duration = None
seconds = None
minutes = None
hours = None
days = None
result_str = None

# запускаем бесконечный цикл, в котором просим пользователя ввести целые числа
# выход из цикла только когда все введенные значения приводятся к типу int
while True:
    duration_list = input('Введите целые числа через пробел: ').split(' ')
    print(duration_list)
    for i in range(len(duration_list)):
        try:
            duration_list[i] = int(duration_list[i])
        except ValueError:
            print('одно из введенных значений не является целым числом. Повторите попытку')
            break
    else:
        break

for duration in duration_list:
    if duration < 60:
        seconds = duration
        result_str = f'{seconds} секунд'
    elif 60 <= duration < 3600:
        minutes = duration // 60
        seconds = (duration % 60) % 60
        result_str = f'{minutes} минут, {seconds} секунд'
    elif 3600 <= duration < 86400:
        hours = duration // 3600
        minutes = (duration % 3600) // 60
        seconds = (duration % 3600) % 60
        result_str = f'{hours} часов, {minutes} минут, {seconds} секунд'
    elif duration >= 86400:
        days = duration // 86400
        hours = (duration % 86400) // 3600
        minutes = ((duration % 86400) % 3600) // 60
        seconds = ((duration % 86400) % 3600) % 60
        result_str = f'{days} дней, {hours} часов, {minutes} минут, {seconds} секунд'

    print(f'{duration} --> {result_str}')
