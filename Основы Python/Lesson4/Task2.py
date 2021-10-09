"""Задание 2"""

import requests


def currency_rates(currency_code):
    """Возвращает курс рубля по отношению к заданной валюте"""

    def currency_parser(res_str):
        """Парсит дату курс"""
        i = 0
        while True:
            pos_cur = res_str.find('<CharCode>', i)
            if pos_cur == -1:
                return None
            i = pos_cur
            currency = res_str[res_str.find('<CharCode>', i) + 10:res_str.find('<CharCode>', i) + 13]
            if currency == currency_code.upper():
                pos_val = res_str.find('<Value>', i)
                value = res_str[res_str.find('<Value>', i) + 7:res_str.find('<Value>', i) + 14]
                value = float(value.replace(',', '.'))
                return value

            i += 1

    res_str = str(requests.get('http://www.cbr.ru/scripts/XML_daily.asp').content, encoding='windows-1251')

    value = currency_parser(res_str)
    return value


currency_name = input('Введите кодировку валюты: ')
print(f'Курс рубля по отношению к {currency_name.upper()} - {currency_rates(currency_name)}')