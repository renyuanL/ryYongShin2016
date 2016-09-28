"""      turtle-example-suite:

         tdemo_round_dance.py
         
(Needs version 1.1 of the turtle module that
comes with Python 3.1)

Dancing turtles have a compound shape
consisting of a series of triangles of
decreasing size.

Turtles march along a circle while rotating
pairwise in opposite direction, with one
exception. Does that breaking of symmetry
enhance the attractiveness of the example?

Press any key to stop the animation.

Technically: demonstrates use of compound
shapes, transformation of shapes as well as
cloning turtles. The animation is
controlled through update().
"""

from turtle_tc import *

def 停止():
    global 正在跑
    正在跑 = 假

def 主函數():
    global 正在跑
    清除幕()
    背景色("gray10")
    追蹤(假)
    形狀("triangle")
    f =   0.793402
    φ = 9.064678
    s = 5
    c = 1
    # create compound shape
    sh = 形狀類("compound")
    for i in 範圍(10):
        形狀大小(s)
        p =取形狀多邊形()
        s *= f
        c *= f
        傾斜(-φ)
        sh.加成員(p, (c, 0.25, 1-c), 黑)
    登記形狀("multitri", sh)
    # create dancers
    形狀大小(1)
    形狀("multitri")
    提筆()
    設位置(0, -200)
    舞者們 = []
    for i in 範圍(180):
        前進(7)
        傾斜(-4)
        左轉(2)
        更新()
        if i % 12 == 0:
            舞者們.append(複製())
    回家()
    # dance
    正在跑 = 真
    在按著鍵時(停止)
    聽()
    cs = 1
    while 正在跑:
        ta = -4
        for 舞者 in 舞者們:
            舞者.前進(7)
            舞者.左轉(2)
            舞者.傾斜(ta)
            ta = -4 if ta > 0 else 2
        if cs < 180:
            右轉(4)
            形狀大小(cs)
            cs *= 1.005
        更新()
    return "DONE!"

if __name__=='__main__':
    印(主函數())
    主迴圈()
    


    
