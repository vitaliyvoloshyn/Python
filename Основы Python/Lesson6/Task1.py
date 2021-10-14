"""
Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>)
"""

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    request_list = []
    for i in f:
        pars_list = i.split()
        request_list.append((pars_list[0], pars_list[5].replace('"', ''), pars_list[6]))
print(request_list)
