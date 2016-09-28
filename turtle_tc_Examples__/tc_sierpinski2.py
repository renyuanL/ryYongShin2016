#!/usr/bin/python
"""       turtle-example-suite:

          tdemo_sierpinski2.py

This program draws a coloured sierpinski
triangle. This version draws the small
filled triangles by stamping a triangle
shaped turtle

Each vertex of the triangle is associated
with a color - in the case of this example
red, green and blue. The colors of the
triangular cells of the Sierpinski triangle
are computed by interpolation.
"""

from turtle_tc import *
from time import clock

class Vec3(tuple):   #######  rudimentary, just as needed
    def __new__(cls, x, y, z):
        return tuple.__new__(cls, (x, y, z))
    def __add__(我, other):
        return Vec3(我[0]+other[0], 我[1]+other[1], 我[2]+other[2])
    def __truediv__(我, other):
        other = float(other)
        return Vec3(我[0]/other, 我[1]/other, 我[2]/other)

def triangle(長度, stufe, f1, f2, f3):  # f1, f2, f3 colors of the vertices
    if stufe == 0:
        顏色((f1+f2+f3)/3)
        蓋章()
    else:
        c12 = (f1+f2)/2
        c13 = (f1+f3)/2
        c23 = (f2+f3)/2
        前進(長度)
        triangle(長度/2, stufe-1, c13, c23, f3)
        後退(長度)
        左轉(120)
        前進(長度)
        triangle(長度/2, stufe-1, c12, c13, f1)
        後退(長度)
        左轉(120)
        前進(長度)
        triangle(長度/2, stufe-1, c23, c12, f2)
        後退(長度)
        左轉(120)

def 主函數():
    設立(640, 640)
    模式(角度從北開始順時針)
    重設()
    設回復暫存區(1)
    色模式(255)
    藏龜()
    提筆()
    速度(0)
    形狀("triangle")
    sierp_size = 600
    h3 = (sierp_size/6.0)*3**0.5

    深度 = 6
    形狀大小(sierp_size/20./(2**深度))
    追蹤(1,0)
    後退(h3/2.0)
    ta = clock()
    triangle(h3, 深度,
            Vec3(255.0,0,0), Vec3(0,255.0,0), Vec3(0,0,255.0))
    追蹤(1)
    tb = clock()
    return "{0:.2f} sec.".format(tb-ta)

if __name__ == '__main__':
    訊息 = 主函數()
    印(訊息)
    主迴圈()

## on my desktop-machine: approx. 0.6 sec.
