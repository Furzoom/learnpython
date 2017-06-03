#!/usr/bin/env python
# -*- coding: utf-8 -*-


from random import randrange, choice
from string import ascii_lowercase as lc
from time import ctime


def gendata():
    f = open('redata.txt', 'w')
    tlds = ('com', 'edu', 'net', 'org', 'gov')

    for i in xrange(randrange(5, 11)):
        dtint = randrange(1 << 32)       # pick date
        dtstr = ctime(dtint)            # date string
        llen = randrange(4, 8)          # login is shorter
        login = ''.join(choice(lc) for j in xrange(llen))
        dlen = randrange(llen, 13)      # domain is longer
        dom = ''.join(choice(lc) for j in xrange(dlen))
        f.write('{}::{}@{}.{}::{}-{}-{}\n'.format(dtstr, login, dom,
                                                  choice(tlds), dtint,
                                                  llen, dlen))
    f.close()

if __name__ == '__main__':
    gendata()
