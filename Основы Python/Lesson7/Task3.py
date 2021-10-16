"""Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
Написать скрипт, который собирает все шаблоны в одну папку templates"""

import os
import shutil

folder = 'my_project'
path_lst = []
for i in os.walk(folder):
    if "templates" in i[0]:
        if len(i[1]):
            for j in i[1]:
                try:
                    shutil.copytree(os.path.join(i[0], j), os.path.join('templates', j))
                except FileExistsError as er:
                    print(er)