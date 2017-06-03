#!/usr/bin/env python
# -*- coding: utf-8 -*-


import socket

HOST = 'localhost'
PORT = 1234
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = raw_input('> ')
    if not data:
        break
    tcpCliSock.send(data)
    data = tcpCliSock.recv(BUFSIZE)
    if not data:
        break
    print(data)


if __name__ == '__main__':
    pass