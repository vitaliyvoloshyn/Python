import utils


def cur(args):
    program, val = args
    x, y = utils.currency_rates(val)
    print(f'Курс рубля по отношению к {val.upper()} - {x}. Дата запроса {y}')
    return 0


if __name__ == '__main__':
    import sys

    exit(cur(sys.argv))
