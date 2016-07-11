#!/usr/bin/env python
# -*- coding: utf-8 -*-

score = int(raw_input('input score: '))

if score > 100 or score < 0:
    print 'Bad score'
elif score >= 90:
    print 'A'
elif score >= 80:
    print 'B'
elif score >= 70:
    print 'C'
elif score >= 60:
    print 'D'
else:
    print 'E'
