"""       turtle-example-suite:

           tdemo_wikipedia3.py

This is the third of a series of 4 examples
inspired by the Wikipedia article on turtle
graphics. (See example wikipedia1 for URLs)

It gives an alternate implementation:
First we create (ne-1) (i.e. 35 in this
example) copies of our first turtle p.
Then we let them perform their steps in
parallel.

Version without cloning using the turtles()
method of TurtleScreen
"""
from turtle_tc import *; from turtle_tc import 幕類, 龜類, 主迴圈
from time import clock

def create_turtles(ne):
    for i in 範圍(ne):
        t=龜類()
        t.藏龜()
        t.速度(0)
        t.設頭向(i*360.0/ne)
        t.筆寬(3)
    return s.龜群()

def mn_eck(ne,sz):
    #create ne turtles
    myturtles = create_turtles(ne)
    for i in 範圍(ne):
        c = abs(ne/2.0-i)/(ne*.7)
        # let alle those turtles make
        # a step in parallel:
        for t in myturtles:
            t.右轉(360./ne)
            t.筆色(1-c,0,c)
            t.前進(sz)

def 主函數():
    global s
    at = clock()
    s = 幕類()
    s.背景色(黑)
    s.追蹤(36, 0)
    mn_eck(36,19)
    et = clock()
    return "Laufzeit: {0:.3f} sec".format(et-at)

if __name__ == '__main__':
    訊息 = 主函數()
    印(訊息)
    主迴圈()


## on my desktop machine: approx. 1.65 sec.
## on my laptop: approx. 1.1 sec
