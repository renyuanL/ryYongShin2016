#!/usr/bin/python
"""       turtle-example-suite:

            tdemo_mill1.py

Demonstrates a user defined 'three winged'
pen. Pen rotates via left() method AND
moves via setpos() method.
Pensize changes via turtlesize() method.

Be patient. (You migkht want to enlarge your
xturtleDemo window or use the canvas'
scrollbars to search for the wheel.)
"""
from turtle_tc import *
from time import clock

WINGSIZE = 135

def 主函數():
    重設()
    藏龜()
    追蹤(0)
    左轉(75)
    提筆()
    前進(WINGSIZE)
    x,y=位置()
    後退(WINGSIZE)
    下筆()

    開始多邊形()
    for i in 範圍(3):
        前進(WINGSIZE)
        左轉(105)
        前進(2*x)
        左轉(105)
        前進(WINGSIZE)
        右轉(90)
    結束多邊形()
    mill=取多邊形()
    登記形狀('mill', mill)

    重設()
    左轉(90)
    提筆()
    前進(60)
    下筆()
    筆粗(20)
    顏色(藍, 黃)
    右轉(15)
    開始填()
    後退(WINGSIZE*1.2)
    右轉(75)
    前進(2*x*1.2)
    左轉(105)
    前進(WINGSIZE*1.2)
    結束填()
    藏龜()


    p=龜類()
    p.藏龜()
    p.提筆()
    p.形狀('mill')
    p.重設大小模式("user")
    p.龜大小(outline=3)
    p.填色(紅)
    p.左轉(90)
    p.前進(60)
    p.顯龜()
    追蹤(真)
    p.速度(10)

    ta = clock()
    anglevel = 2
    for i in 範圍(180):
        p.左轉(anglevel)

    tb = clock()
    尺寸因子 = 1
    vel = 1
    for i in 範圍(200):
        anglevel += .3
        p.左轉(anglevel)
        if i > 60:
            尺寸因子 *= 0.985
            vel *=1.01
            x,y = p.位置()
            p.設位置(x+vel,y+vel)
            p.龜大小(尺寸因子)
    tc = clock()
    return "Runtime: %.1fsec. / %.1fsec." % (tb-ta, tc-tb)

if __name__ == '__main__':
    訊息 = 主函數()
    印(訊息)
    主迴圈()    

## on my laptop: 6 sec. / 12.4 sec
