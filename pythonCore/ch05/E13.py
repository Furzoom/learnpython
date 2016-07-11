#!/usr/bin/env python
# -*- coding: utf-8 -*-


def time_split(t):
    hour, minute = t.split(':')
    minutes = int(hour) * 60 + int(minute)
    return minutes


if __name__ == '__main__':
    print time_split('0:25')
    print time_split('13:00')
    print time_split('4:4')
