#!/usr/bin/env python
# -*- coding: utf-8 -*-


import re


def test1():
    re_obj = re.compile('(\d+)-(\d+)')
    m = re_obj.match('188-1112-8888')
    print(type(m))
    print(type(m.group()))
    print(m.group())
    print(m.groups())

    m = re_obj.match('(010)88884567')
    if m is not None:
        print(m.group())

    m = re_obj.match('tel:188-1112-7777')
    if m is not None:
        print(m.group())

    m = re_obj.search('tel:188-1112-7777')
    if m is not None:
        print('matches: {}'.format(m.group()))


def test2():
    re_obj = re.compile('bit|bat|bet')
    m = re_obj.match('bat')
    if m is not None:
        print('1: {}'.format(m.group()))

    m = re_obj.match('blt')
    if m is not None:
        print('2: {}'.format(m.group()))

    m = re_obj.match('He bit me!')
    if m is not None:
        print('3: {}'.format(m.group()))

    m = re_obj.search('He bit me!')
    if m is not None:
        print('4: {}'.format(m.group()))


def test3():
    re_obj = re.compile('.end')
    m = re_obj.match('bend')
    if m is not None:
        print('1: {}'.format(m.group()))

    m = re_obj.match('end')
    if m is not None:
        print('2: {}'.format(m.group()))

    m = re_obj.match('\nend')
    if m is not None:
        print('3: {}'.format(m.group()))

    m = re_obj.search('the end')
    if m is not None:
        print('4: {}'.format(m.group()))


def test4():
    # re_obj = re.compile('\w+@\w+\.com')
    # re_obj = re.compile('\w+@(\w+\.)?\w+\.com')
    re_obj = re.compile('\w+@(\w+\.)*\w+\.com')
    m = re_obj.match('mn@furzoom.com')
    if m is not None:
        print('1 {}'.format(m.group()))

    m = re_obj.match('mn@lab.furzoom.com')
    if m is not None:
        print('2 {}'.format(m.group()))

    m = re_obj.match('mn@test.lab.furzoom.com')
    if m is not None:
        print('3 {}'.format(m.group()))


def test5():
    re_obj = re.compile('(\w{3})-(\d{3})')
    m = re_obj.match('abc-123')

    print('group() {}'.format(m.group()))
    print('group(1) {}'.format(m.group(1)))
    print('group(2) {}'.format(m.group(2)))
    print('groups() {}'.format(m.groups()))


def test6():
    re_obj = re.compile('(\d+?)-(\d+)')
    m = re_obj.findall('123-456-7-09')
    if m is not None:
        print('1 {}'.format(m))

    m = re_obj.finditer('123-456-7-09')
    print(m.next().groups())
    print(m.next().groups())


def test7():
    re_obj = re.compile(r'[\r\n]')
    m = re_obj.sub('', 'hello\r\n \rWorld!\n')
    print('1 {}'.format(m))

    re_obj = re.compile(r'(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})')
    m = re_obj.sub(r'\2/\1/\3', '2/20/1991')
    print('2 {}'.format(m))


def test8():
    m = re.split(':', 'str1:str2:str3')
    print('1 {}'.format(m))

    data = (
        'Mountain View, CA 94040',
        'Sunnyvale, CA',
        'Los Altos, 94023',
        'Cupertino 95014',
        'Palo Alto CA',
        )
    for datum in data:
        print re.split(', |(?= (?:\d{5}|[A-Z]{2})) ', datum)


def test8():
    print(re.findall('(?i)yes', 'yes? Yes, YES!!'))
    print(re.findall('(?mi)(^th[\w ]+)', 'This line\nThat line'))
    print(re.findall('(?s)th.+', 'The first line\nthe second line\nthe third line'))
    print(re.search(r'''(?x)
            \((\d{3})\)
            [ ]
            (\d{3})
            -
            (\d{4})
            ''', '(800) 555-1212').groups())

    print(re.findall(r'http://(?:\w+\.)*(\w+\.com)',
          'http://google.com http://www.google.com http://code.oa.google.com'))


def test9():
    print(bool(re.search(r'(?:(x)|y)(?(1)y|x)', 'xy')))
    print(bool(re.search(r'(?:(x)|y)(?(1)y|x)', 'yx')))
    print(bool(re.search(r'(?:(x)|y)(?(1)y|x)', 'xx')))
    print(bool(re.search(r'(?:(x)|y)(?(1)y|x)', 'yy')))


def test10():
    re_obj = re.compile('^(Mon|Tue|Wen|Thu|Fri|Sat|Sun)')
    data = 'Thu Mar 22 09:15:18 1984::xqxpb@svoey.net::448766118-5-5'
    m = re_obj.match(data)
    if m is not None:
        print(m.group())
        print(m.groups())

    print('-' * 78)
    re_obj = re.compile('^(\w{3})')
    m = re_obj.match(data)
    if m is not None:
        print(m.group())
        print(m.groups())

    print('-' * 78)
    re_obj = re.compile('.+?(\d+-\d+-\d+)$')
    m = re_obj.search(data)
    if m is not None:
        print(m.group())
        print(m.groups())

    print('-' * 78)

if __name__ == '__main__':
    # test1()
    # print('-' * 78)
    # test2()
    # print('-' * 78)
    # test3()
    # print('-' * 78)
    # test4()
    # print('-' * 78)
    # test5()
    # print('-' * 78)
    # test6()
    # print('-' * 78)
    # test7()
    # print('-' * 78)
    # test8()
    # print('-' * 78)
    # test8()
    # print('-' * 78)
    # test9()
    print('-' * 78)
    test10()
