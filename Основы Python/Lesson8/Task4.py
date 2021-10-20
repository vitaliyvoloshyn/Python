from functools import wraps
"""Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции и 
выбрасывать исключение ValueError, если что-то не так
Примечание: сможете ли вы замаскировать работу декоратора?"""
def val_checker(i):
    def val_checker_(fn):
        @wraps(fn)
        def wrapper(n):
            try:
                if i(n):
                    return fn(n)
                else:
                    raise ValueError
            except ValueError:
                print('ValueError: wrong val')
        return wrapper
    return val_checker_
   
@val_checker(lambda x: x > 0) 
def calc_cube(x):
    return x**3
    
print(f'Функция {calc_cube.__name__} -> {calc_cube(8)}')
