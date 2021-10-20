import re

"""*(вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
для получения информации вида: 
(<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>), """


def pars_log_file():
    with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            # print(line)
            # print(i)
            ip = re.match(r'^\S+\s', line)[0][:-1]
            # print(ip)
            req_dt = re.search(r"\[.+\]", line)[0][1:-1]
            # print(req_dt)
            req_type = re.search(r'\"\w+', line)[0][1:]
            # print((req_type))
            req_res = re.search(r'/downloads/\w+', line)[0]
            # print((req_res))
            resp_code = re.search(r'\s(\d+)\s(\d+)\s', line)[1]
            # print((resp_code))
            resp_size = re.search(r'\s(\d+)\s(\d+)\s', line)[2]
            # print((resp_size))
            parsed_raw = (ip, req_dt, req_type, req_res, resp_code, resp_size)
            print(parsed_raw)


pars_log_file()
