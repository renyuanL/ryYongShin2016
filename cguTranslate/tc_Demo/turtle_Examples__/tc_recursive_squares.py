"""      turtle-example-suite:

        tdemo_recursive squares.py

This program draws a recursive pattern of
coloured squares, that have smaller squares
at their vertices. To each square size
belongs a different colour.

The squares are stamped, the larger ones
first, the smaller ones upon them.

Finally you see 5461 squares.
"""
from turtle_tc import *; from turtle_tc import 龜類, 幕類
from time import clock

顏色們 = [紅, 綠, 藍, 黃,
          青, 紫, "gray60"]

def recsquare(l, f, 顏色們):
    if not 顏色們: return
    t.形狀大小(l/20)
    t.顏色(顏色們[0])
    t.蓋章()
    t.前進(l/2.0)
    t.左轉(90)
    t.前進(l/2)
    t.左轉(90)
    for _ in 範圍(4):
        recsquare(l*f, f, 顏色們[1:])
        t.前進(l)
        t.左轉(90)
    t.右轉(90)
    t.後退(l/2)
    t.右轉(90)
    t.後退(l/2)
    if len(顏色們) == 5:
        s.更新()

def 主函數():
    global s, t
    s = 幕類()
    s.背景色("gray10")
    t = 龜類(visible=假, shape=方形)
    t.提筆()
    t.速度(0)
    s.追蹤(假)
    ta = clock()
    recsquare(256, 0.5, 顏色們)
    tb = clock()
    return "{0:.2f}sec.".format(tb-ta)

if __name__ == "__main__":
    主函數()
    s.主迴圈()
