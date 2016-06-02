#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Spam:
    numInstance = 0
    def __init__(self):
        Spam.numInstance = Spam.numInstance + 1
    @staticmethod
    def printNumInstance():
        print("Number of instances craeted: ", Spam.numInstance)

if __name__ == '__main__':
    a,b,c = Spam(), Spam(), Spam()
    Spam.printNumInstance()
    a.printNumInstance()
