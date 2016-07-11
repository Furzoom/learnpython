#!/usr/bin/env python
# -*- coding: utf-8 -*-


def payment(account, consumption):
    print 'Pymt#  Paid   Balance'
    print '----- ------ ---------'
    num = int(account / consumption) + 1
    for i in range(num + 1):
        if i == 0:
            paid = 0
            balance = account
        elif i == num:
            paid = balance
        else:
            paid = consumption

        balance -= paid
        print '%-5d $%5.2f  $%6.2f' % (i, paid, balance)


if __name__ == '__main__':
    payment(100, 16.13)