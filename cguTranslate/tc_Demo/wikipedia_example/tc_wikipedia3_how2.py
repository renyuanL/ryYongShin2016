"""       turtle-example-suite:

        tdemo_wikipedia3_how2.py

This is a variant of the third of a series of
4 examples inspired by the Wikipedia article on
turtle graphics. (See example wikipedia1 for URLs)

It's essentially the same as example
wikipedia3, but for fewer polygons with
fewer edges.

It show graphically how it works, by
using normal speed and tracer(1). So
it's execution time is (intentionally) much
longer.
"""
from turtle_tc import *
from time import clock

def mn_eck(p, ne,sz):
    龜列表 = [p]
    for i in 範圍(1, ne):
        q = p.複製()
        q.右轉(360.0/ne)
        龜列表.append(q)
        p = q
    for i in 範圍(ne):
        c = abs(ne/2.0-i)/(ne*.7)
        for t in 龜列表:
            t.右轉(360./ne)
            t.筆色(1-c,0,c)
            t.前進(sz)

def 主函數():
    s = 幕類()
    s.背景色(黑)
    p=龜類()
    p.筆色(紅)
    p.筆粗(3)
    p.速度(1)

    s.追蹤(1,10)
#    print p.speed(), p.delay()

    at = clock()
    mn_eck(p, 13,39)   # or: (7,60)
    et = clock()
    return "Laufzeit: {0:.3f} sec".format(et-at)

if __name__ == '__main__':
    訊息 = 主函數()
    印(訊息)
    主迴圈()


## on my machine: approx. 48 sec.
