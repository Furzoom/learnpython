#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Echo server program
"""

import socket
import time
import os

HOST = ''
PORT = 50007


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # enable address reuse
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1)
    while True:
        conn, addr = s.accept()
        print('Connected by {}'.format(addr))
        while True:
            data = conn.recv(1024)
            if not data:
                break
            elif data == 'date':
                data = get_date()
            elif data == 'os':
                data = get_os()
            elif data.startswith('ls'):
                data = get_ls(data[2:])

            conn.sendall(data)
        conn.close()

    s.close()


def get_date():
    return time.ctime()


def get_os():
    return os.name


def get_ls(dire):
    if not dire.strip():
        dire = os.curdir

    return '\n'.join(os.listdir(dire.strip()))


if __name__ == '__main__':
    main()
