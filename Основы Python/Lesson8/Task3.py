from functools import wraps

"""Написать декоратор для логирования типов позиционных аргументов функции
Примечание: если аргументов несколько - выводить данные о каждом через запятую;
можете ли вы вывести тип значения функции? 
Сможете ли решить задачу для именованных аргументов? 
Сможете ли вы замаскировать работу декоратора? 
Сможете ли вывести имя функции"""


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for i in args:
            try:
                res = func(i)
            except TypeError:
                res = None
            finally:
                print(f'{func.__name__}({i}: {type(i)}, результат {res}: {type(res)})')

        for i in kwargs.values():
            try:
                res = func(i)
            except TypeError:
                res = None
            finally:
                print(f'{func.__name__}({i}: {type(i)}, результат {res}: {type(res)})')

    return wrapper


@type_logger
def calc_cube(n):
    return n ** 3


calc_cube(5, 10, 67, 'hj', True, (34, 34), ['fg', 45], {'fg': 67}, encod=23, encod_=[56, 8, 34])
print(calc_cube)
