#!/usr/bin/env python
# -*- coding: utf-8 -*-


import socket


HOST = 'localhost'
PORT = 1234
BUFSIZE = 1024
ADDR = (HOST, PORT)

udpCliSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    data = raw_input('> ')
    if not data:
        break
    udpCliSock.sendto(data, ADDR)
    data, addr = udpCliSock.recvfrom(BUFSIZE)
    if not data:
        break
    print(data)

