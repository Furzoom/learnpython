#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import MySQLdb
import json
import logging

from multiprocessing import Pool

# db config
HOST = '127.0.0.1'
PORT = 3306
USERNAME = 'root'
PASSWORD = '123456'
DB = 'jd_comment'

# project config
MAX_PAGE = 9999
PROCESS_NUM = 4
product_id_list = [3717578]

_url_template = 'http://sclub.jd.com/comment/productPageComments.action?productId={}&score=0&sortType=3&page={}&pageSize=10'
_sql_template = ('INSERT INTO items(product_id, product_name, score, content)'
                 'VALUES(%s, %s, %s, %s)')
con = MySQLdb.connect(host=HOST, port=PORT, user=USERNAME, passwd=PASSWORD, db=DB, charset='utf8')
cur = con.cursor()


def get_product_comments_by_id(product_id):
    first_page_data = get_page(0, product_id)
    total_pages = first_page_data.get('maxPage', 1) if first_page_data.get('maxPage', 1) < MAX_PAGE else MAX_PAGE
    save_page_to_db(first_page_data)

    for page_number in xrange(1, total_pages):
        try:
            data = get_page(page_number, product_id)
            save_page_to_db(data)
        except Exception as e:
            log.error(e)
            continue


def save_page_to_db(data):
    comments_list = get_comments_list(data)
    save_comments_list_to_db(comments_list)


def get_page(page_number, product_id):
    try:
        data = urllib2.urlopen(_url_template.format(product_id, page_number))
        log.info(data)
        return json.load(data, encoding='gbk')
    except Exception as e:
        log.error(e)


def get_comments_list(data):
    comments_list = data.get('comments', [])
    return [[item.get('referenceId', ''), item.get('referenceName', ''),
             item.get('score', 0), item.get('content', '')]
            for item in comments_list]


def save_comments_list_to_db(comments_list):
    map(save_to_db, comments_list)


def save_to_db(args_list):
    try:
        cur.execute(_sql_template, tuple(args_list))
        con.commit()
    except Exception as e:
        log.error(e)


if __name__ == '__main__':
    format = '%(lineno)s %(message)s'
    logging.basicConfig(format=format)
    log = logging.getLogger()
    try:
        processing_pool = Pool(PROCESS_NUM)
        processing_pool.map(get_product_comments_by_id, product_id_list)
        processing_pool.close()
        processing_pool.join()
    except Exception as e:
        log.error(e)
    finally:
        cur.close()
        con.close()
