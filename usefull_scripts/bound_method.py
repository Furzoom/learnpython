#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Spam:
    def doit(self, message):
        print(message)

class Eggs:
    def m1(self, n):
        print(n)

    def m2(self):
        x = self.m1
        x(42)

class Foo:
    def __init__(self):
        self.x = 1

    def display(msg):
        print(msg.x)

class Selfless:
    def __init__(self, data):
        self.data = data

    def selfless(arg1, arg2):
        return arg1 + arg2

    def normal(self, arg1, arg2):
        return self.data + arg1 + arg2

class Number:
    def __init__(self, base):
        self.base = base
    def double(self):
        return self.base ** 2
    def triple(self):
        return self.base ** 3

def square(arg):
    return arg ** 2

class Sum:
    def __init__(self, val):
        self.val = val
    def __call__(self, arg):
        return self.val + arg

class Product:
    def __init__(self, val):
        self.val = val
    def method(self, arg):
        return self.val * arg

class Negate:
    def __init__(self, val):
        self.val = -val
    def __repr__(self):
        return str(self.val)


if __name__ == "__main__":
    obj = Spam()
    obj.doit('hello')
    x = obj.doit
    x('world')
    cls = Spam.doit
    cls(obj, 'welcome')

    Eggs().m2()

    Foo().display()

    x = Selfless(2)
    print(x.normal(3, 4))
    print(Selfless.selfless(3, 4))

    x, y, z = Number(2), Number(3), Number(4)
    print(x.double())
    acts = [x.double, y.double, y.triple, z.double]
    for act in acts:
        print(act())
    bound = x.double
    print(bound.__self__, bound.__func__)
    print(bound.__self__.base)
    print(bound())

    sobject = Sum(2)
    pobject = Product(3)
    actions = [square, sobject, pobject.method, Negate]
    for act in actions:
        print(act(5))

    table = {act(5): act for act in actions}
    for (key, value) in table.items():
        print('{0} => {1}'.format(key, value))



