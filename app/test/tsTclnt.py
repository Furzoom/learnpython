#!/usr/bin/env python
# -*- coding: utf-8 -*-


import socket
import sys

BUFSIZE = 1024


def start_client(address):
    tcpCliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpCliSock.connect(address)

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
    host = '127.0.0.1'
    port = 1234

    if len(sys.argv) == 2:
        host = sys.argv[1]
    elif len(sys.argv) == 3:
        host = sys.argv[1]
        port = int(sys.argv[2])
    start_client((host, port))
