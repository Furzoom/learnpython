#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import abstractmethod

class Super:
    def delegate(self):
        self.action()
    def action(self):
        #assert False, 'action must be defined!'
        #
        raise NotImplementedError('action must be defined!')
    @abstractmethod
    def method(self):
        pass

if __name__ == '__main__':
    x = Super()
    x.delegate()
