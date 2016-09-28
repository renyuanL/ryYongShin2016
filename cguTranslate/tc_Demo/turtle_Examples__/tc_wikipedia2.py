"""      turtle-example-suite:

          tdemo_wikipedia2.py

This is the second of a series of 4 examples
inspired by the Wikipedia article on turtle
graphics. (See example wikipedia1 for URLs)

To the plain transcription of the
corresponding Logo code I added the lines:

        c = abs(ne/2.0-i)/(ne*.7)
        pencolor(1-c,0,c)

in n_eck. They change the colors or the
circle segments.

"""
from turtle_tc import *
from time import clock

def n_eck(ne,sz):
    for i in 範圍(ne):
        右轉(360./ne)
        # blue component of color it i-th
        # segment:
        c = abs(ne/2.0-i)/(ne*.7)
        筆色(1-c,0,c)
        前進(sz)

def mn_eck(ne, sz):
    for i in 範圍(ne):
        右轉(360./ne)
        n_eck(ne, sz)

def 主函數():
    模式(角度從北開始順時針)
    速度(0)
    藏龜()
    背景色(黑)
    筆色(紅)
    筆粗(3)

    追蹤(36,0)

    at = clock()
    mn_eck(36,20)
    et = clock()
    return "Laufzeit: {0:.3f} sec".format(et-at)

if __name__ == '__main__':
    訊息 = 主函數()
    印(訊息)
    主迴圈()


## on my desktop machine: approx. 1.2 sec.
