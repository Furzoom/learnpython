#!/usr/bin/env python
# -*- coding: utf-8 -*-
import select
import socket
import Queue

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_address = ('192.168.80.233', 8080)
server.bind(server_address)
server.listen(10)

inputs = [server]
outputs = []
message_queues = {}
timeout = 20

while True:
    print "Waiting for connecting..."
    readable, writable, exceptional = select.select(inputs, outputs, inputs, timeout)

    if not (readable or writable or exceptional):
        print "select timeout, select..."
        continue

    # read event
    for s in readable:
        # if server
        if s is server:
            connection, client_address = s.accept()
            print "new connection: ", client_address
            connection.setblocking(0)
            inputs.append(connection)
            message_queues[connection] = Queue.Queue()
        else:
            data = s.recv(1024)
            if data:
                print "Receive data: ", data, "Client: ", s.getpeername()
                message_queues[s].put(data)
                if s not in outputs:
                    outputs.append(s)
            else:
                print "close connection: ", client_address
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                s.close()
                del message_queues[s]
    for s in writable:
        try:
            msg = message_queues[s].get_nowait()
        except Queue.Empty:
            print "connect: ", s.getpeername(), "message queue is empty"
            outputs.remove(s)
        else:
            print "Send data: ", msg, "to", s.getpeername()
            s.send(msg)
    for s in exceptional:
        print "connection exception:", s.getpeername()
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()
        del message_queues[s]

