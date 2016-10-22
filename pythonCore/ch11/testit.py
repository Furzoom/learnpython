__author__ = 'MN'

def testit(func, *args, **kwargs):
    try:
        retval = func(*args, **kwargs)
        result = (True, retval)
    except Exception as e:
        result = (False, str(e))
    return result


def test():
    funcs = (int, float)
    vals = (1234, 12.34, '1234', '12.34')

    for eachFunc in funcs:
        print('-' * 20)
        for eachVal in vals:
            retval = testit(eachFunc, eachVal)
            if retval[0]:
                print('{}({}) = {}'.format(eachFunc.__name__, repr(eachVal), retval[1]))
            else:
                print('{}({}) = FAILED: {}'.format(eachFunc.__name__, repr(eachVal), retval[1]))


if __name__ == '__main__':
    test()

