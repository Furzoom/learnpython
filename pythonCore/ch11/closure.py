#!/usr/bin/env python
# -*- coding: utf-8 -*-


def counter(start_at = 0):
    count = [start_at]

    def incr():
        count[0] += 1
        return count[0]
    return incr


def test():
    count = counter(5)
    print(count())
    print(count())
    count2 = counter(100)
    print(count2())
    print(count())


def make_adder(addend):
    def adder(augend):
        return addend + augend
    return adder


def test2():
    p = make_adder(23)
    q = make_adder(44)
    print(p(100))
    print(q(100))


if __name__ == '__main__':
    test()
    test2()
