#!/usr/bin/env python
# -*- coding: utf-8 -*-


def cal_interest(capital):
    interest = 0.001
    return capital * (1 + interest) ** 365


if __name__ == '__main__':
    print cal_interest(100)
