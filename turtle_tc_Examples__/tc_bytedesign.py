#!/usr/bin/python
"""      turtle-example-suite:

        tdemo_bytedesign.py

An example adapted from the example-suite
of PythonCard's turtle graphcis.

It's based on an article in BYTE magazine
Problem Solving with Logo: Using Turtle
Graphics to Redraw a Design
November 1982, p. 118 - 134

-------------------------------------------

Due to the statement

t.getscreen).delay(0)

in line 152, which sets the animation delay
to 0, this animation runs in "line per line"
mode as fast as possible.
"""

import math
from turtle_tc import *; from turtle_tc import 龜類, 主迴圈
from time import clock

# wrapper for any additional drawing routines
# that need to know about each other
class 設計師類(龜類):

    def 設計(我, 家的位置, 比例尺度):
        我.提筆()
        for i in 範圍(5):
            我.前進(64.65 * 比例尺度)
            我.下筆()
            我.輪子(我.位置(), 比例尺度)
            我.提筆()
            我.後退(64.65 * 比例尺度)
            我.右轉(72)
        我.提筆()
        我.前往(家的位置)
        我.右轉(36)
        我.前進(24.5 * 比例尺度)
        我.右轉(198)
        我.下筆()
        我.中央塊(46 * 比例尺度, 143.4, 比例尺度)
        我.取幕().追蹤(真)

    def 輪子(我, 開始位置, 比例尺度):
        我.右轉(54)
        for i in 範圍(4):
            我.五之塊(開始位置, 比例尺度)
        我.下筆()
        我.左轉(36)
        for i in 範圍(5):
            我.三之塊(開始位置, 比例尺度)
        我.左轉(36)
        for i in 範圍(5):
            我.下筆()
            我.右轉(72)
            我.前進(28 * 比例尺度)
            我.提筆()
            我.後退(28 * 比例尺度)
        我.左轉(54)
        我.取幕().更新()

    def 三之塊(我, 開始位置, 比例尺度):
        舊頭向 = 我.頭向()
        我.下筆()
        我.後退(2.5 * 比例尺度)
        我.右三邊形(31.5 * 比例尺度, 比例尺度)
        我.提筆()
        我.前往(開始位置)
        我.設頭向(舊頭向)
        我.下筆()
        我.後退(2.5 * 比例尺度)
        我.左三邊形(31.5 * 比例尺度, 比例尺度)
        我.提筆()
        我.前往(開始位置)
        我.設頭向(舊頭向)
        我.左轉(72)
        我.取幕().更新()

    def 五之塊(我, 開始位置, 比例尺度):
        舊頭向 = 我.頭向()
        我.提筆()
        我.前進(29 * 比例尺度)
        我.下筆()
        for i in 範圍(5):
            我.前進(18 * 比例尺度)
            我.右轉(72)
        我.右五邊形(18 * 比例尺度, 75, 比例尺度)
        我.提筆()
        我.前往(開始位置)
        我.設頭向(舊頭向)
        我.前進(29 * 比例尺度)
        我.下筆()
        for i in 範圍(5):
            我.前進(18 * 比例尺度)
            我.右轉(72)
        我.左五邊形(18 * 比例尺度, 75, 比例尺度)
        我.提筆()
        我.前往(開始位置)
        我.設頭向(舊頭向)
        我.左轉(72)
        我.取幕().更新()

    def 左五邊形(我, 邊, 角度, 比例尺度):
        if 邊 < (2 * 比例尺度): return
        我.前進(邊)
        我.左轉(角度)
        我.左五邊形(邊 - (.38 * 比例尺度), 角度, 比例尺度)

    def 右五邊形(我, 邊, 角度, 比例尺度):
        if 邊 < (2 * 比例尺度): return
        我.前進(邊)
        我.右轉(角度)
        我.右五邊形(邊 - (.38 * 比例尺度), 角度, 比例尺度)

    def 右三邊形(我, 邊, 比例尺度):
        if 邊 < (4 * 比例尺度): return
        我.前進(邊)
        我.右轉(111)
        我.前進(邊 / 1.78)
        我.右轉(111)
        我.前進(邊 / 1.3)
        我.右轉(146)
        我.右三邊形(邊 * .75, 比例尺度)

    def 左三邊形(我, 邊, 比例尺度):
        if 邊 < (4 * 比例尺度): return
        我.前進(邊)
        我.左轉(111)
        我.前進(邊 / 1.78)
        我.左轉(111)
        我.前進(邊 / 1.3)
        我.左轉(146)
        我.左三邊形(邊 * .75, 比例尺度)

    def 中央塊(我, s, a, 比例尺度):
        我.前進(s); 我.左轉(a)
        if s < (7.5 * 比例尺度):
            return
        我.中央塊(s - (1.2 * 比例尺度), a, 比例尺度)

def 主函數():
    t = 設計師類()
    t.速度(0)
    t.藏龜()
    t.取幕().延遲(0)
    t.取幕().追蹤(0)
    at = clock()
    t.設計(t.位置(), 2)
    et = clock()
    return "執行時間: %.2f 秒。" % (et-at)

if __name__ == '__main__':
    訊息 = 主函數()
    印(訊息)
    主迴圈()
