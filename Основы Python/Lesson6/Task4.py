"""
*(вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ.
Только теперь не нужно создавать словарь с данными. Вместо этого нужно сохранить объединенные данные в новый файл
(users_hobby.txt). Хобби пишем через двоеточие и пробел после ФИО:
"""

import sys


def user_hobby(user_file='users.csv', hobby_file='hobby.csv', out_file='users_hobby.txt'):
    def user():
        with open(user_file, 'r', encoding='utf-8') as user_f:
            for line_user in user_f:
                yield line_user.strip()


    def hobby():
        with open(hobby_file, 'r', encoding='utf-8') as hobby_f:
            for line_hobby in hobby_f:
                yield line_hobby.strip()

    user_ = user()
    hobby_ = hobby()

    with open(out_file, 'w', encoding='utf-8') as f:
        while True:
            try:
                us = next(user_)
            except StopIteration:
                sys.exit()
            try:
                hob = next(hobby_)
            except StopIteration:
                hob = None

            f.write(f'{us}: {hob}\n')

if __name__ == '__main__':
    user_hobby()