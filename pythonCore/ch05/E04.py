#!/usr/bin/env python
# -*- coding: utf-8 -*-


def leap_year(year):
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False


if __name__ == '__main__':
    year = int(raw_input('year: '))
    if leap_year(year):
        print 'Leap year'
    else:
        print 'Not a leap year'
