"""Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего"""

from random import randint


def create_list(n: int = 100):
    """Возвращает список рандомных чисел от 1 до 1000 длинною n элементов"""
    out = [randint(1, 1000) for i in range(n)]
    return out


def list_processing(lst):
    """Возвращает обработанный исходный список"""
    out_list = [lst[i] for i in range(1, len(lst)) if lst[i] > lst[i - 1]]
    return out_list


if __name__ == '__main__':
    orig_list = create_list()
    print(orig_list)
    processed_list = list_processing(orig_list)
    print(processed_list)
