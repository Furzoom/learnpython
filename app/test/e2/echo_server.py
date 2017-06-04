#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Echo server program
"""

import socket

HOST = ''
PORT = 50007


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    while True:
        conn, addr = s.accept()
        print('Connected by {}'.format(addr))
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
        conn.close()

    s.close()

if __name__ == '__main__':
    main()
