#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket


def main():
    HOST = '192.168.80.233'
    PORT = 21567
    BUFSIZ = 1024
    ADDR = (HOST, PORT)

    tcpCliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    while True:
        data = raw_input('> ')
        if not data:
            break
        tcpCliSock.send(data)
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        print(data)
    tcpCliSock.close()


if __name__ == '__main__':
    main()

