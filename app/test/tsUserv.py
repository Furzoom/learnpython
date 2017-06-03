#!/usr/bin/env python
# -*- coding: utf-8 -*-


import socket
import time

HOST = ''
PORT = 1234
BUFSIZE = 1024
ADDR = (HOST, PORT)

udpSerSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print('Waiting for message...')
    try:
        data, addr = udpSerSock.recvfrom(BUFSIZE)
    except KeyboardInterrupt as e:
        print('server is closing...')
        udpSerSock.close()
        break
    udpSerSock.sendto('[{}] {}'.format(time.ctime(), data), addr)
    print('...received from add returned to:', addr)


