#!/usr/bin/env python
# -*- coding: utf-8 -*-


def cal_coins(dollar):
    dollar = int(dollar * 100)
    coins = []
    coins.append(dollar / 25)
    dollar %= 25
    coins.append(dollar / 10)
    dollar %= 10
    coins.append(dollar / 5)
    dollar %= 5
    coins.append(dollar)
    return tuple(coins)


if __name__ == '__main__':
    dollar = float(raw_input('input dollar: '))
    coins = cal_coins(dollar)
    print '{0} quarter(s), {1} dime(s), {2} nickel(s) and {3} penny(s)'.format(*coins)
