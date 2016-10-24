__author__ = 'MN'

def foo():
    print('\ncalling foo()...')
    aString = 'bar'
    anInt = 42
    print('foo()\'s globals: {}'.format(globals().keys()))
    print('foo()\'s locals: {}'.format(locals().keys()))

print('__main__\'s globals: {}'.format(globals().keys()))
print('__main__\'s locals: {}'.format(locals().keys()))
foo()
