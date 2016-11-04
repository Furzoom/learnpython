#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# v0.1
#while True:
#    reply = input("Enter text:")
#    if reply == 'stop':
#        break
#    print(int(reply) ** 2)
#print('Bye')

# v0.2
#while True:
#    reply = input("Enter text:")
#    if reply == 'stop':
#        break
#    elif not reply.isdigit():
#        print('Bad!' * 8)
#    else:
#        print(int(reply) ** 2)
#print('Bye')

# v0.3
while True:
    reply = raw_input("Enter text:")
    if reply == 'stop':
        break
    try:
        num = int(reply)
    except:
        print('Bad!' * 8)
    else:
        print(num ** 2)
print('Bye')


