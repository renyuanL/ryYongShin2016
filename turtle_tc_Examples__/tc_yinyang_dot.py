#!/usr/bin/python
"""        turtle-example-suite:

           tdemo_yinyang_dot.py

Another drawing suitable as a beginner's
programming example.

The small circles are drawn by the dot
command. For an alternative solution
using the circle command see example
yinyang_circle.

"""

from turtle_tc import *

def 陰(半徑, 顏色1, 顏色2):
    筆寬(3)
    顏色(顏色1)
    開始填()
    畫圓(半徑/2., 180)
    畫圓(半徑, 180)
    左轉(180)
    畫圓(-半徑/2., 180)
    結束填()
    顏色(顏色2)
    左轉(90)
    提筆()
    前進(半徑/2.)
    點(半徑/4.)
    後退(半徑/2.)
    下筆()
    左轉(90)

def yinyang(半徑, 顏色1, 顏色2):
    陰(半徑, 顏色1, 顏色2)
    陰(半徑, 顏色2, 顏色1)

def 主函數():
    重設()
    速度(0)
    藏龜()
    背景色(.4,.1,0)
    yinyang(200, 藍, 黃)
    藏龜()
    return "Done!"

if __name__ == '__main__':
    主函數()
    主迴圈()
