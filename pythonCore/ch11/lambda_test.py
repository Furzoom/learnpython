__author__ = 'MN'


def test():
    data = range(10)
    ret = filter(lambda x: x % 2, data)
    for x in ret:
        print(x)

if __name__ == '__main__':
    test()
