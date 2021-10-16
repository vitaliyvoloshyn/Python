"""(вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи те же,
а значения — кортежи вида (<files_quantity>, [<files_extensions_list>])
Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт."""

import os
import json

folder = os.getcwd()

# Создаем словарь - абс.путь к файлу : размер файла
dict_files = {os.path.join(files[0], file): os.stat(os.path.join(files[0], file))[6] / 1024 for files in os.walk(folder) for file in files[2]}

# находим максимальный размер файла
max_size = max(dict_files.values())
# создаем словарь для сортировки файлов по размеру
# заполняем только ключи (градиент) отталкиваясь от максимального размера файла
i = 10
sort_dict = {}
while i < max_size*10:
    sort_dict[i] = [0,[]]
    i *= 10
# заполняем значения словаря - определяем кол-во файлов, размер которых находится в диапазоне ключей и
# формируем вложенный список расширений файлов
for path, size in dict_files.items():
    for j in sort_dict:
        if size < j:
            sort_dict[j][0] = sort_dict[j][0] + 1
            sort_dict[j][1].append(os.path.splitext(path)[1])
            break
# приводим словарь в надлежащий вид - удаляем повторяющиеся расширения файлов и приводим ключи к tuple
for key, val in sort_dict.items():
    sort_dict[key][1] = list(set(val[1]))
    sort_dict[key] = tuple(sort_dict[key])
# сохранение результатов в файл
out_file_name = os.path.basename(folder) + '_summary.json'
with open(out_file_name, 'w', encoding='utf-8') as f:
    json.dump(sort_dict, f)
print(f'Результаты сохранены в файл {os.path.join(folder, out_file_name)}')