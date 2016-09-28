"""      turtle-example-suite:

          tdemo_wikipedia4.py

This example is inspired by the Wikipedia
article on turtle graphics.
(See example wikipedia1 for URLs)

First we create (ne-1) (i.e. 35 in this
example) copies of our first turtle p.
Then we let them perform their steps in
parallel.

Followed by a complete undo().
"""
from turtle_tc import *; from turtle_tc import 幕類, 龜類, 主迴圈
from time import clock, sleep

def mn_eck(p, ne,sz):
    龜列表 = [p]
    #create ne-1 additional turtles
    for i in 範圍(1,ne):
        q = p.複製()
        q.右轉(360.0/ne)
        龜列表.append(q)
        p = q
    for i in 範圍(ne):
        c = abs(ne/2.0-i)/(ne*.7)
        # let those ne turtles make a step
        # in parallel:
        for t in 龜列表:
            t.右轉(360./ne)
            t.筆色(1-c,0,c)
            t.前進(sz)

def 主函數():
    s = 幕類()
    s.背景色(黑)
    p=龜類()
    p.速度(0)
    p.藏龜()
    p.筆色(紅)
    p.筆粗(3)

    s.追蹤(36,0)

    at = clock()
    mn_eck(p, 36, 19)
    et = clock()
    z1 = et-at

    sleep(1)

    at = clock()
    while any([t.回復暫存區的個數() for t in s.龜群()]):
        for t in s.龜群():
            t.回復()
    et = clock()
    return "Laufzeit: %.3f sec" % (z1+et-at)


if __name__ == '__main__':
    訊息 = 主函數()
    印(訊息)
    主迴圈()
