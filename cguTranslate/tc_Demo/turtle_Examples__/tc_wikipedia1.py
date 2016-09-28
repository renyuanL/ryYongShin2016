"""      turtle-example-suite:

          tdemo_wikipedia1.py

This is the first of a series of 4 examples
inspired by the Wikipedia article on turtle
graphics:

http://en.wikipedia.org/wiki/Turtle_graphics
http://en.wikipedia.org/wiki/Image:Remi_turtlegrafik.png

It's a plain transcription of the
corresponding Logo code.

"""
from turtle_tc import *
from time import clock

def n_eck(ne,sz):
    for i in 範圍(ne):
        右轉(360./ne)
        前進(sz)

def mn_eck(ne, sz):
    for i in 範圍(ne):
        右轉(360./ne)
        n_eck(ne, sz)
        
def 主函數():
    #mode("logo")
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

# on my desktop machine: approx. 0.3 sec.
