import fileinput
import os
import sys

file_name = 'bakery.csv'


def add_sale(sales_amount):
    with open(file_name, 'a', encoding='utf-8') as f:
        f.write(str(sales_amount) + '\n')


def show_sales(*args):
    args = [int(i) for i in args]
    if len(args) == 0:
        from_, to_ = 1, None
    elif len(args) == 1:
        from_, to_ = int(args[0]), None
    elif len(args) == 2:
        from_, to_ = args

    with open(file_name, 'r', encoding='utf-8') as f:
        i = 1
        for line in f:
            if not to_:
                if i >= from_:
                    print(line.strip())
            else:
                if from_ <= i <= to_:
                    print(line.strip())
            i += 1


def change(num_line, value):
    check = False
    with open(file_name, 'r', encoding='utf-8') as f:
        with open('temp.csv', 'w', encoding='utf-8') as tf:
            for i, line_str in enumerate(f):
                if i == int(num_line) - 1:
                    tf.write(str(value) + '\n')
                    check = True
                else:
                    tf.write(line_str)

    if check:
        os.remove(file_name)
        os.rename('temp.csv', file_name)
    else:
        os.remove('temp.csv')
        print(f'Строки с номером {num_line} нет в файле')


def main(args):
    if args[1] == 'add':
        add_sale(args[2])
    elif args[1] == 'show':
        if len(args) > 2:
            show_sales(*args[2:])
        else:
            show_sales()
    elif args[1] == 'change':
        change(args[2], args[3])
    elif args[1] == 'help':
        print("""Основные команды скрипта:
add <значение> - добавить значение в файл;
show <номер строки С> <номер строки По> - без параметров отображает все строки, с одним параметром отображает строки С,
                                            с двумя параметрами отображает строки С и По;
change - <номер строки> <значение> - замена значения в строке на новое значение;
help - справка по командам скрипта""")


# add_sale(958.6)
# change(11, 666.2)
# show_sales(0)


if __name__ == '__main__':
    exit(main(sys.argv))
