#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb

try:
    conn = MySQLdb.connect(host='localhost',user='root',passwd='123456',db='test',port=3306,charset='utf8mb4')
    cur = conn.cursor()
    value = (1, 10)
#    sql = 'insert into t value(%s,%s)'
#    cur.execute(sql, value)
#    values = []
#    for i in xrange(20):
#        values.append((i, i*2))
#
#    cur.executemany(sql, values)
    count = cur.execute('select * from user')
    print(count)
    for row in cur:
        print(row)
        print(row[1])
    conn.commit()
    cur.close()
    conn.close()
except MySQLdb.Error, e:
    print("Mysql Error {0}: {1}".format(e.args[0], e.args[1]));
