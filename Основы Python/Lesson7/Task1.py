"""Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:

|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp

Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); как лучше хранить конфигурацию
 этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект; можно ли будет при этом расширять
  конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?"""

"""
конфигурацию стартера, считаю целесообразным, хранить в файле (starter_dirs.txt)
"""

import os


def file_structure(config_file):
    with open(config_file, 'r', encoding='utf-8') as f:
        for line in f:
            if line.endswith('\\\n') or line.endswith('\\'):
                try:
                    os.makedirs(line.strip())
                except FileExistsError:
                    pass
            else:
                x = open(line.strip(), 'w')
                x.close()


if __name__ == '__main__':
    file_structure('starter_dirs.txt')
