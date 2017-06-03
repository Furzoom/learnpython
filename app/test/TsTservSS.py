#!/usr/bin/env python
# -*- coding: utf-8 -*-

import SocketServer
import time


HOST = ''
PORT = 1234
ADDR = (HOST, PORT)


class MyRequestHandler(SocketServer.StreamRequestHandler):
    def handle(self):
        print('...connected from: {}'.format(self.client_address))
        self.wfile.write('[{}] {}'.format(time.ctime(),
                                          self.rfile.readline()))


if __name__ == '__main__':
    tcpServ = SocketServer.TCPServer(ADDR, MyRequestHandler)
    print('waiting fro connection...')
    tcpServ.serve_forever()

