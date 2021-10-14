import Task4


def user_hobby_(args):
    Task4.user_hobby(args[1], args[2], args[3])


if __name__ == '__main__':
    import sys

    exit(user_hobby_(sys.argv))
