#!/usr/bin/python
"""        turtle-example-suite:

           tdemo_radioactive.py

A simple drawing, suitable as a beginner's
programming example.
Therefore the animation is set to slow
by the command speed(1). So you can easily
follow each and every action of the turtle.

Be patient!
"""

from turtle_tc import *

def square(length):
    for i in 範圍(4):
        前進(length)
        左轉(90)

def sector(半徑, 角度):
    前進(半徑)
    左轉(90)
    畫圓(半徑, 角度)
    左轉(90)
    前進(半徑)
    左轉(180-角度)

def 移動(x, y):
    提筆()
    前進(x)
    左轉(90)
    前進(y)
    右轉(90)
    下筆()

def radioactive(radius1, radius2, 邊,
        角度=60, outlinecol=黑, fillcol=黃):
    顏色(outlinecol)
    移動(-(邊/2) , -(邊/2))
    
    開始填()
    square(邊)
    顏色(fillcol)
    結束填()
    移動((邊/2), (邊/2))
    顏色(outlinecol)
    右轉(90 + 角度/2)

    for i in 範圍(3):
        開始填()
        sector(radius1,角度)
        左轉(120)
        #left((360 - 3 * angle)/3 + 60)
        顏色(outlinecol)
        結束填()

    提筆()
    前進(radius2)
    左轉(90)
    下筆()

    顏色(fillcol)
    開始填()
    畫圓(radius2)
    顏色(outlinecol)
    結束填()

    提筆()
    左轉(90)
    前進(radius2)
    筆寬(1)

def 主函數():
    重設()
    筆寬(5)
    速度(1)
    radioactive(160, 36, 400)
    return "Done!"

if __name__ == '__main__':
    訊息 = 主函數()
    印(訊息)
    主迴圈()


