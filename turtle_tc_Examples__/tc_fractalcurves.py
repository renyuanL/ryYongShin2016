#!/usr/bin/python
"""      turtle-example-suite:

        tdemo_fractalCurves.py

This program draws two fractal-curve-designs:
(1) A hilbert curve (in a box)
(2) A combination of Koch-curves.

The CurvesTurtle class and the fractal-curve-
methods are taken from the PythonCard example
scripts for turtle-graphics.
"""
from turtle_tc import *
from time import sleep, clock

class 曲線龜類(筆類):
    # example derived from
    # Turtle Geometry: The Computer as a Medium for Exploring Mathematics
    # by Harold Abelson and Andrea diSessa
    # p. 96-98
    def hilbert(我, 尺寸, 等級, 對等性):
        if 等級 == 0:
            return
        # rotate and draw first subcurve with opposite parity to big curve
        我.左轉(對等性 * 90)
        我.hilbert(尺寸, 等級 - 1, -對等性)
        # interface to and draw second subcurve with same parity as big curve
        我.前進(尺寸)
        我.右轉(對等性 * 90)
        我.hilbert(尺寸, 等級 - 1, 對等性)
        # third subcurve
        我.前進(尺寸)
        我.hilbert(尺寸, 等級 - 1, 對等性)
        # fourth subcurve
        我.右轉(對等性 * 90)
        我.前進(尺寸)
        我.hilbert(尺寸, 等級 - 1, -對等性)
        # a final turn is needed to make the turtle
        # end up facing outward from the large square
        我.左轉(對等性 * 90)

    # Visual Modeling with Logo: A Structural Approach to Seeing
    # by James Clayson
    # Koch curve, after Helge von Koch who introduced this geometric figure in 1904
    # p. 146
    def 碎形多邊形(我, n, 弳度, lev, dir):
        import math

        # if dir = 1 turn outward
        # if dir = -1 turn inward
        邊緣 = 2 * 弳度 * math.sin(math.pi / n)
        我.提筆()
        我.前進(弳度)
        我.下筆()
        我.右轉(180 - (90 * (n - 2) / n))
        for i in 範圍(n):
            我.碎形(邊緣, lev, dir)
            我.右轉(360 / n)
        我.左轉(180 - (90 * (n - 2) / n))
        我.提筆()
        我.後退(弳度)
        我.下筆()

    # p. 146
    def 碎形(我, 距離, 深度, dir):
        if 深度 < 1:
            我.前進(距離)
            return
        我.碎形(距離 / 3, 深度 - 1, dir)
        我.左轉(60 * dir)
        我.碎形(距離 / 3, 深度 - 1, dir)
        我.右轉(120 * dir)
        我.碎形(距離 / 3, 深度 - 1, dir)
        我.左轉(60 * dir)
        我.碎形(距離 / 3, 深度 - 1, dir)

def 主函數():
    ft = 曲線龜類()

    ft.重設()
    ft.速度(0)
    ft.藏龜()
    ft.取幕().追蹤(1,0)
    ft.提筆()

    尺寸 = 6
    ft.設位置(-33*尺寸, -32*尺寸)
    ft.下筆()

    ta=clock()
    ft.填色(紅)
    ft.開始填()
    ft.前進(尺寸)

    ft.hilbert(尺寸, 6, 1)

    # frame
    ft.前進(尺寸)
    for i in 範圍(3):
        ft.左轉(90)
        ft.前進(尺寸*(64+i%2))
    ft.提筆()
    for i in 範圍(2):
        ft.前進(尺寸)
        ft.右轉(90)
    ft.下筆()
    for i in 範圍(4):
        ft.前進(尺寸*(66+i%2))
        ft.右轉(90)
    ft.結束填()
    tb=clock()
    res =  "Hilbert: %.2fsec. " % (tb-ta)

    sleep(3)

    ft.重設()
    ft.速度(0)
    ft.藏龜()
    ft.取幕().追蹤(1,0)

    ta=clock()
    ft.顏色(黑, 藍)
    ft.開始填()
    ft.碎形多邊形(3, 250, 4, 1)
    ft.結束填()
    ft.開始填()
    ft.顏色(紅)
    ft.碎形多邊形(3, 200, 4, -1)
    ft.結束填()
    tb=clock()
    res +=  "Koch: %.2fsec." % (tb-ta)
    return res

if __name__  == '__main__':
    訊息 = 主函數()
    印(訊息)
    主迴圈()
