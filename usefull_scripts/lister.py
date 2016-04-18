#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

class ListInstance:
    """
    Mix-in class
    """
    def __str__(self):
        return '<Instance of %s, address %s:\n%s>' % (
                self.__class__.__name__,
                id(self),
                self.__attrnames())

    def __attrnames(self):
        result = ''
        for attr in dir(self):
            if attr[:2] == '__' and attr[-2:] == '__':
                result += '\tname %s=<>\n' % attr
            else:
                result += '\tname %s=%s\n' % (attr, getattr(self, attr))
        return result

class Spam(ListInstance):
    def __init__(self):
        self.data1 = 'food'

class Super:
    def __init__(self):
        self.data1 = 'spam'
    def ham(sefl):
        pass

class Sub(Super, ListInstance):
    def __init__(self):
        Super.__init__(self)
        self.data2 = 'eggs'
        self.data3 = 42
    def spam(self):
        pass


if __name__ == '__main__':
    x, y = Spam(), Spam()
    print(x)
    print(y)

    x = Sub()
    print(x)
