"""(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield."""

from Task1 import iteration_of_gen

num = 20
my_gen = (i for i in range(1, num, 2))

iteration_of_gen(my_gen)
