#!/usr/bin/env python
# -*- coding: utf-8 -*-


def read_text_file():
    # get filename
    fname = raw_input('Enter filename: ')
    print

    # attempt to open file for reading
    try:
        fobj = open(fname, 'r')
    except IOError, e:
        print '*** file open error:', e
    else:
        # display contents to the screen
        for eachline in fobj:
            print eachline,
        fobj.close()


def write_text_file():
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
    all_content = []
    print "\nEnter lines ('.' by itself quit).\n"

    # loop until user terminates input
    while True:
        entry = raw_input('> ')
        if entry == '.':
            break
        else:
            all_content.append(entry)

    # write lines to file with proper line-endling
    fobj = open(fname, 'w')
    fobj.writelines(['%s%s' % (x, ls) for x in all_content])
    fobj.close()
    print 'DONE!'


if '__main__' == __name__:
    item = ''
    while True:
        print '(1) Write to file'
        print '(2) Read from file'
        print '(x) Exit'
        item = raw_input('> ')
        if item == '1':
            write_text_file()
        elif item == '2':
            read_text_file()
        elif item == 'x' or item == 'X':
            break
        else:
            continue
