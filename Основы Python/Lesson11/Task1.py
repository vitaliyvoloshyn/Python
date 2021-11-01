import re
import datetime


class Date:

    def __init__(self, value):

        Date.valid_date(value)
        self.date_obj = Date.convert_type(value)

    @classmethod
    def convert_type(cls, value):
        try:
            return datetime.datetime.strptime(value, '%d-%m-%Y')
        except ValueError as er:
            print(er)

    @staticmethod
    def valid_date(value):
        pass
        # print(__date_val)
        if not re.match(r'\d{1,2}-\d{1,2}-\d{4}', value):
            raise TypeError('Неверный формат данных')


c = Date('20-11-2019')
print(c.date_obj)
