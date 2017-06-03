#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from demo.polygon import Point


class PointTest(unittest.TestCase):
    def setUp(self):
        self.p1 = Point(0, 0)
        self.p2 = Point(3, 4)

    def tearDown(self):
        pass

    def testSub(self):
        p = self.p2 - self.p1
        self.assertEqual(p.x, 3)
        self.assertEqual(p.y, 4)

    def testAdd(self):
        p = self.p1 + self.p2
        self.assertEqual(p.x, 3)
        self.assertEqual(p.y, 4)

    def testXy(self):
        self.assertEqual(self.p1.xy, (0, 0))
        self.assertEqual(self.p2.xy, (3, 4))

    def testStr(self):
        self.assertEqual(str(self.p1), 'x = 0, y = 0')
        self.assertEqual(str(self.p2), 'x = 3, y = 4')

    def testDist(self):
        d = Point.dist(self.p1, self.p2)
        self.assertEqual(d, 5)



if __name__ == '__main__':
    unittest.main()
