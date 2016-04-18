#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import requests
#r = requests.get('http://letiantian.me/')
#print(r.text)

import gevent
from gevent import monkey
monkey.patch_socket()

import urllib2

urls = ['http://letiantian.me/'] * 10

def get_content(url):
    data = urllib2.urlopen(url).read()
    return data

#for url in urls:
#    get_content(url)

jobs = [gevent.spawn(get_content, url) for url in urls]
gevent.joinall(jobs)


