#!/usr/bin/env python
# -*- coding: utf-8 -*-


from twisted.internet import protocol, reactor
import time

PORT = 1234


class TSServProtocol(protocol.Protocol):

    def __init__(self):
        self.clnt = None

    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print('...connected from: {}'.format(clnt))

    def dataReceived(self, data):
        self.transport.write('[{}] {}'.format(time.ctime(), data))


if __name__ == '__main__':
    factory = protocol.Factory()
    factory.protocol = TSServProtocol
    print('waiting for connection...')
    reactor.listenTCP(PORT, factory)
    reactor.run()
