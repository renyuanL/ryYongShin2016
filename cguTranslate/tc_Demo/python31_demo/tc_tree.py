#!/usr/bin/python
"""      turtle-example-suite:

             tdemo_tree.py

Displays a 'breadth-first-tree' - in contrast
to the classical Logo tree drawing programs,
which use a depth-first-algorithm.

Uses:
(1) a tree-generator, where the drawing is
quasi the side-effect, whereas the generator
always yields None.
(2) Turtle-cloning: At each branching point the
current pen is cloned. So in the end there
are 1024 turtles.
"""
from turtle_tc import *; from turtle_tc import 龜類, 主迴圈
from time import clock

def 樹(p列表, l, a, f):
    """ plist is list of pens
    l is length of branch
    a is half of the angle between 2 branches
    f is factor by which branch is shortened
    from level to level."""
    if l > 3:
        列表 = []
        for p in p列表:
            p.前進(l)
            q = p.複製()
            p.左轉(a)
            q.右轉(a)
            列表.append(p)
            列表.append(q)
        for x in 樹(列表, l*f, a, f):
            yield 無

def 製造樹():
    p = 龜類()
    p.設回復暫存區(無)
    p.藏龜()
    p.速度(0)
    p.取幕().追蹤(30,0)
    p.左轉(90)
    p.提筆()
    p.前進(-210)
    p.下筆()
    t = 樹([p], 200, 65, 0.6375)
    for x in t:
        pass
    印(len(p.取幕().龜群()))

def 主函數():
    a=clock()
    製造樹()
    b=clock()
    return "done: %.2f sec." % (b-a)

if __name__ == "__main__":
    訊息 = 主函數()
    印(訊息)
    主迴圈()
