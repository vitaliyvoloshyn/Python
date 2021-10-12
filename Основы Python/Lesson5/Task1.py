"""Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield"""


def gen_num(n):
    for i in range(1, n, 2):
        yield i


def iteration_of_gen(gen):
    print(type(gen))
    while True:
        try:
            print(next(gen))
        except StopIteration:
            print('Конец итерации')
            break


if __name__ == '__main__':
    num = 20
    my_gen = gen_num(num)
    iteration_of_gen(my_gen)
