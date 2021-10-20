import re

"""Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает 
имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря. 
Если адрес не валиден, выбросить исключение ValueError. """


def email_pars(mail):
    pattern = re.compile(r'[\d\w\-\*\.]+@[\d\w]+\.[\w]+')
    valid = re.fullmatch(pattern, mail)
    if not valid:
        try:
            raise ValueError
        except ValueError as er:
            print(f'ValueError: {er} wrong email: {mail}')
            exit()
    else:
        user_name, domain = re.split(r'@', mail)
        out_dict = {'username': user_name, 'domain': domain}
        return out_dict


print(email_pars('nobody_2345@gmail.com'))
