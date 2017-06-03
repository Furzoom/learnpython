#!/usr/bin/env python
# -*- coding: utf-8 -*-


import socket

# ss = socket()
# ss.bind()
# ss.listen()
# inf_loop:
#     cs = ss.accept()
#     comm_loop:
#         cs.recv()/cs.send()
#     cs.close()
# ss.close()

def create():
    tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


if __name__ == '__main__':
    create()
