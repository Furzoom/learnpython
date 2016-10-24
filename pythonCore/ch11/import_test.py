__author__ = 'MN'

def test():
    if True:
        sys = __import__('sys')
        print(help(sys))

if __name__ == '__main__':
    test()
