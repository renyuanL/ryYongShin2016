#!/usr/bin/python
"""       turtle-example-suite:

              tdemo_mill1.py

Demonstrates a user defined 'three winged'
pen. Pen rotates via left() command (as usual).
"""
from turtle_tc import *

def 主函數():
    重設()
    速度(1)
    左轉(75)

    # create three-winged shape for
    # new turtle
    開始多邊形()
    for i in 範圍(3):
        前進(100)
        if i == 0:
            x=x座標() # turtle 'measures' length of
                     # half basis of triangle
        左轉(105)
        前進(2*x)
        左轉(105)
        前進(100)
        右轉(90)
    結束多邊形()
    登記形狀('mill', 取多邊形())

    # the mill
    重設()
    形狀('mill')
    重設大小模式("user")
    龜大小(outline=5)
    速度(1)
    左轉(90)
    提筆()
    後退(120)
    下筆()
    筆粗(20)
    筆色(藍)
    前進(180)
    
    # the wheel ...
    提筆()
    顏色(綠,紅)
    # .. rotates
    anglevel=3.6
    速度(5)
    for i in 範圍(360):
        左轉(anglevel)
        anglevel-=0.0098
    return "Done!"

if __name__ == '__main__':
    訊息 = 主函數()
    印(訊息)
    主迴圈()
