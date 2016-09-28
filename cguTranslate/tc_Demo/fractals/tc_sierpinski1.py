#!/usr/bin/python
"""       turtle-example-suite:

          tdemo_sierpinski1.py

This program draws a coloured sierpinski
triangle.

Each vertex of the triangle is associated
with a color - in the case of this example
red, green and blue. The colors of the
triangular cells of the Sierpinski triangle
are computed by interpolation.

This interpolation uses a 3-vector class
similar to the 2-vector class, which is part
of the turtle graphics module.
"""

from turtle_tc import *
from time import clock

class Vec3(tuple):

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
        開始填()
        for i in 範圍(3):
            前進(長度)
            左轉(120)
        結束填()
    else:
        c12 = (f1+f2)/2
        c13 = (f1+f3)/2
        c23 = (f2+f3)/2
        triangle(長度 / 2, stufe - 1, f1, c12, c13)
        前進(長度)
        左轉(120)
        triangle(長度 / 2, stufe - 1, f2, c23, c12)
        前進(長度)
        左轉(120)
        triangle(長度 / 2, stufe - 1, f3, c13, c23)
        前進(長度)
        左轉(120)

def 主函數():
    設立(720, 720)
    重設()
    設回復暫存區(1)
    sierp_size = 600
    色模式(255)
    速度(0)
    藏龜()
    提筆()
    後退(sierp_size*0.5)
    左轉(90)
    後退(sierp_size*0.4)
    右轉(90)
    追蹤(1,0)
    ta = clock()
    triangle(sierp_size, 6,
            Vec3(255.0,0,0), Vec3(0,255.0,0), Vec3(0,0,255.0))
    tb = clock()
    return "{0:.2f} sec.".format(tb-ta)

if __name__ == '__main__':
    訊息 = 主函數()
    印(訊息)
    主迴圈()


## on my desktop-machine: approx. 1.5 sec.
