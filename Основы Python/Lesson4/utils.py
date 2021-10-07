import requests
from datetime import datetime


def currency_rates(currency_code):
    """Возвращает курс рубля по отношению к заданной валюте"""

    def date_parser(str_date: str):
        """Парсит дату запроса"""
        date_str = str_date.replace(',', '')
        pars_date = datetime.strptime(date_str, '%a %d %b %Y %H:%M:%S %Z')
        return pars_date


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

    header = dict(requests.get('http://www.cbr.ru/scripts/XML_daily.asp').headers)
    res_date = header['Date']
    value = currency_parser(res_str)
    res_date = date_parser(res_date)

    return value, res_date


