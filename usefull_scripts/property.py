#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Person:
    def __init__(self, name):
        self._name = name
    def getName(self):
        print('fetch...')
        return self._name
    def setName(self, value):
        print('change...')
        self._name = value
    def delName(self):
        print('remove...')
        del self._name
    name = property(getName, setName, delName, 'name property docs')

class D:
    'docstring here'
    def __get__(*args):
        print('get')
    def __set__(*args):
        raise AttributeError('cannot set')

class C:
    a = D()

class Name:
    "name descriptor docs"
    def __get__(self, instance, owner):
        print('fetch...')
        return instance._name
    def __set__(self, instance, value):
        print('change...')
        instance._name = value
    def __delete__(self, instance):
        print('remove...')
        del instance._name

class Person2:
    def __init__(self, name):
        self._name = name
    name = Name()


if __name__ == '__main__':
    def testPerson():
        bob = Person('Bob Smith')
        print(bob.name)
        bob.name = 'Robert Smith'
        print(bob.name)
        del bob.name
        print('-' * 20)
        sue = Person('Sue jones')
        print(sue.name)
        print(Person.name.__doc__)

    def testC():
        x = C()
        x.a
        C.a
        print(list(x.__dict__.keys()))
        print(C.a.__doc__)
        try:
            x.a = 99
        except AttributeError as e:
            print(e)
        print(x.a)
        print(list(x.__dict__.keys()))

    def testPerson2():
        bob = Person2('Bob Smith')
        print(bob.name)
        bob.name = 'Robert Smith'
        print(bob.name)
        del bob.name
        print('-' * 20)
        sue = Person2('Sue jones')
        print(sue.name)
        print(Name.__doc__)




    #testPerson()
    #testC()
    testPerson2()

