#!/usr/bin/env python
# -*- coding: utf-8 -*-

from operator import add
from operator import sub
from random import choice
from random import randint


ops = {'+': add, '-': sub}
MAXTRIES = 2


def doprob():
    op = choice('+-')
    nums = [randint(1, 10) for i in range(2)]
    nums.sort(reverse=True)
    ans = ops[op](*nums)
    pr = '%d %s %d =' % (nums[0], op, nums[1])
    oops = 0
    while True:
        try:
            if int(raw_input(pr)) == ans:
                print 'correct'
                break
            if oops == MAXTRIES:
                print 'answer\n%s %d' % (pr, ans)
            else:
                print 'incorrect... try again'
                oops += 1
        except (KeyboardInterrupt, EOFError, ValueError) as e:
            print 'invalid input... try again'


def main():
    while True:
        doprob()
        try:
            opt = raw_input('Again? [y]').lower()
            if opt and opt[0] == 'n':
                break
        except (KeyboardInterrupt, EOFError):
            break


if __name__ == '__main__':
    main()
