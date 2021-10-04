"""
Задание 2
(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с числительными,
начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
~>>> num_translate_adv("One")
"Один"
~>>> num_translate_adv("two")
"два"
"""


def num_translate(*args):
    """Переводит числительные с английского на русский по шаблону с учетом регистра"""
    dist_correspond = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }
    for i in args:
        if not dist_correspond.get(i.lower()):
            print(f'{i} --> {dist_correspond.get(i)}')
        else:
            print(f'{i} --> '
                  f'{dist_correspond.get(i.lower()) if i.islower() else dist_correspond.get(i.lower()).title()}')


num_translate('One', 'two', 'Three', 'four', 'five', 'Six', 'seven', 'eight', 'Nine', 'ten', 'twenty', 'Hundred')
