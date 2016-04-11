#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import sys

template1 = 'My {1[spam]} runs {0.platform}'.format(sys, {'spam': 'laptop'})
template2 = 'My {config[spam]} runs {sys.platform}'.format(sys=sys,
        config={'spam': 'laptop'})

print(template1)
print(template2)
