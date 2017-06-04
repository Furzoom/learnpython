#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Echo client program
"""

import socket

HOST = 'localhost'
PORT = 50007


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    while True:
        data = raw_input('> ')
        if not data:
            break
        s.sendall(data)
        data = s.recv(1024)
        if not data:
            break

        print('{}'.format(data))
    s.close()

if __name__ == '__main__':
    main()
