#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from time import ctime


def t1():
    re_obj = re.compile(r'[bh][aiu]t')
    print(re_obj.match('bat').group())
    print(re_obj.match('bit').group())
    print(re_obj.match('but').group())
    print(re_obj.match('hat').group())
    print(re_obj.match('hit').group())
    print(re_obj.match('hut').group())


def t2():
    re_obj = re.compile(r'[a-zA-Z-]+ [a-zA-Z-]+')
    print(re_obj.match('Ma Dan').group())
    print(re_obj.match('Daney-Li Tang').group())


def t3():
    re_obj = re.compile(r'[a-zA-Z-]+, [a-zA-Z-]+')
    print(re_obj.match('Ma, Dan').group())
    print(re_obj.match('Dan, M').group())


def t4():
    re_obj = re.compile(r'[a-zA-Z_][\w]*')
    print(re_obj.match('a').group())
    print(re_obj.match('__init').group())
    print(re_obj.match('_8K_lsd912').group())


def t5():
    re_obj = re.compile(r'(\d+) ([\w\s]+)')
    print(re_obj.match('1180 Bordeaux Drive').group())
    print(re_obj.match('3120 De la Cruz Boulevard').group())


def t6():
    re_obj = re.compile(r'http://www\.[a-zA-Z1-9-]+\.(com|edu)/')
    print(re_obj.match('http://www.google.com/').group())
    print(re_obj.match('http://www.yahoo.com/').group())
    print(re_obj.match('http://www.mit.edu/').group())


def get_type(data):
    re_obj = re.compile(r'<type \'(\w+)\'>')
    m = re_obj.match(str(data))
    if m is not None:
        return m.group(1)
    else:
        return None


def t13():
    print(get_type(type(3)))
    print(get_type(type(dir)))
    print(get_type(type('1')))
    print(get_type(type(t13)))


def t14():
    re_obj = re.compile(r'1[0-2]')
    print(re_obj.match('10').group())
    print(re_obj.match('11').group())
    print(re_obj.match('12').group())
    m = re_obj.match('13')
    if m is not None:
        print(m.group())


def t17():
    tlds = {'Mon': 0, 'Tue': 0, 'Wed': 0, 'Thu': 0, 'Fri': 0,
            'Sat': 0, 'Sun': 0}
    with open('redata.txt', 'r') as f:
        for line in f:
            m = re.match(r'^(\w{3}).*', line)
            if m is not None:
                tlds[m.group(1)] += 1

    for (k, v) in tlds.items():
        print('{}: {}'.format(k, v))


def t18():
    with open('redata.txt', 'r') as f:
        for line in f:
            m = re.match(r'(.+)::.*::(\d+)-.+', line)
            if m is not None:
                if ctime(int(m.group(2))) == m.group(1):
                    print('match')
                else:
                    print('not match')


def t19():
    with open('redata.txt', 'r') as f:
        for line in f:
            m = re.search(r'::(\d+)', line)
            if m is not None:
                print(m.group(1))


def t20():
    with open('redata.txt', 'r') as f:
        for line in f:
            m = re.search(r'::(.*)::', line)
            if m is not None:
                print(m.group(1))


def t21():
    with open('redata.txt', 'r') as f:
        for line in f:
            m = re.match(r'^.{4}(\w{3})', line)
            if m is not None:
                print(m.group(1))


def t22():
    with open('redata.txt', 'r') as f:
        for line in f:
            m = re.search(r'(\d{4})::', line)
            if m is not None:
                print(m.group(1))


def t28():
    re_obj = re.compile(r'(\d{3}-|\(\d{3}\))?(\d{3}-\d{4})')
    m = re_obj.match('555-1212')
    if m is not None:
        print(m.group())
    m = re_obj.match('800-555-1212')
    if m is not None:
        print(m.group())
    m = re_obj.match('(800)555-1212')
    if m is not None:
        print(m.group())


if __name__ == '__main__':
    # print('-' * 78)
    # print('t1')
    # t1()
    # print('-' * 78)
    # print('t2')
    # t2()
    # print('-' * 78)
    # print('t3')
    # t3()
    # print('-' * 78)
    # print('t4')
    # t4()
    # print('-' * 78)
    # print('t5')
    # t5()
    # print('-' * 78)
    # print('t6')
    # t6()
    # print('-' * 78)
    # print('t13')
    # t13()
    # print('-' * 78)
    # print('t14')
    # t14()
    # print('-' * 78)
    # print('t17')
    # t17()
    # print('-' * 78)
    # print('t18')
    # t18()
    # print('-' * 78)
    # print('t19')
    # t19()
    # print('-' * 78)
    # print('t20')
    # t20()
    # print('-' * 78)
    # print('t21')
    # t21()
    # print('-' * 78)
    # print('t22')
    # t22()
    print('-' * 78)
    print('t28')
    t28()
