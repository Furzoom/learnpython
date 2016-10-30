#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wx
import math
from abc import ABCMeta
from abc import abstractmethod


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    @property
    def xy(self):
        return (self.x, self.y)

    def __str__(self):
        return 'x = {}, y = {}'.format(self.x, self.y)

    def __repr__(self):
        return str(self.xy)

    @staticmethod
    def dist(a, b):
        return math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)


class Polygon(object):
    __metaclass__ = ABCMeta

    def __init__(self, points_list, **kwargs):
        for point in points_list:
            assert isinstance(point, Point), 'input must be Point type'
        self.points = points_list[:]
        self.points.append(points_list[0])
        self.color = kwargs.get('color', '#000000')

    def drawPoints(self):
        points_xy = [point.xy for point in self.points]
        print(points_xy)
        return tuple(points_xy)

    @abstractmethod
    def area(self):
        pass

    def __lt__(self, other):
        assert isinstance(other, Polygon)
        return self.area < other.area


class RectAngle(Polygon):
    def __init__(self, startPoint, w, h, **kwargs):
        self._w = w
        self._h = h
        rect = [startPoint, startPoint + Point(w, 0),
                startPoint + Point(w, h), startPoint + Point(0, h)]
        Polygon.__init__(self, rect, **kwargs)

    def area(self):
        return self._w * self._w


class Frame(wx.Frame):
    def __init__(self, title, shapes):
        super(Frame, self).__init__(None, title=title, size=(600, 400))
        self.shapes = shapes
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Center()
        self.Show()

    def OnPaint(self, e):
        dc = wx.PaintDC(self)
        for shape in self.shapes:
            dc.SetPen(wx.Pen(shape.color))
            dc.DrawLines(shape.drawPoints())


if __name__ == '__main__':
    prepare_draws = []
    start_p = Point(50, 60)
    a = RectAngle(start_p, 100, 80, color='#FF0000')
    prepare_draws.append(a)

    print(Point.dist(start_p, Point(100, 100)))

    for shape in prepare_draws:
        print(shape.area())

    app = wx.App()
    Frame('Shapes', prepare_draws)
    app.MainLoop()
