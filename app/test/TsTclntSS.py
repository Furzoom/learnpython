#!/usr/bin/env python
# -*- coding: utf-8 -*-


import socket

HOST = 'localhost'
PORT = 1234
ADDR = (HOST, PORT)
BUFSIZE = 1024

while True:
    tcpCliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = raw_input('> ')
    if not data:
        break

    tcpCliSock.send('{}\r\n'.format(data))
    data = tcpCliSock.recv(BUFSIZE)
    if not data:
        break

    print(data.strip())
    tcpCliSock.close()
