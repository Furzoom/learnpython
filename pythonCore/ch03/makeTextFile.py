#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""makeTextFile.py -- create text file
"""

import os

ls = os.linesep
fname = ''

# get filename
while True:
    fname = raw_input('Input filename: ')
    if os.path.exists(fname):
        print "ERROR: '%s' already exists" % fname
    else:
        break

# get file content (text) lines
allContent = []
print "\nEnter lines ('.' by itself quit).\n"

# loop until user terminates input
while True:
    entry = raw_input('> ')
    if entry == '.':
        break
    else:
        allContent.append(entry)

# write lines to file with proper line-endling
fobj = open(fname, 'w')
fobj.writelines(['%s%s' % (x, ls) for x in allContent])
fobj.close()
print 'DONE!'
