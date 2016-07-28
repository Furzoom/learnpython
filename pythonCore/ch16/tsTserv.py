#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
from time import ctime

def main():
    HOST = ''
    PORT = 21567
    BUFSIZ = 1024
    ADDR = (HOST, PORT)

    tcpSerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpSerSock.bind(ADDR)
    tcpSerSock.listen(5)

    while True:
        print('waiting for connection...')
        tcpCliSock, addr = tcpSerSock.accept()
        print(addr)
        while True:
            data = tcpCliSock.recv(BUFSIZ)
            if not data:
                break
            tcpCliSock.send('[%s] %s' % (ctime(), data))

        tcpCliSock.close()
    tcpSerSock.close()


if __name__ == '__main__':
    main()

