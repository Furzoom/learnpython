#!/usr/bin/env python
# -*- coding: utf-8 -*-


import socket
import time


HOST = ''
PORT = 1234
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)


while True:
    print('waiting for connection...')
    tcpClient, addr = tcpSerSock.accept()
    print('...connected from: {}'.format(addr))
    while True:
        data = tcpClient.recv(BUFSIZE)
        if not data:
            break
        tcpClient.send('[{}] {}'.format(bytes(time.ctime(), 'utf-8'), data))
    tcpClient.close()

# tcpSerSock.close()
