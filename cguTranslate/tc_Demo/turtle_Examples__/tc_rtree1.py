#!/usr/bin/python
"""      turtle-example-suite:

            tdemo_rtree1.py

Displays a 'breadth-first-tree' - in contrast
to the classical Logo tree drawing programs,
which use a depth-first-algorithm.

Uses turtle-cloning: At each branching point the
current turtle is cloned. 
"""
from turtle_tc import *; from turtle_tc import 龜類, 幕類
from time import clock

幕 = 幕類()

def 樹(p列表, l, a, f):
    """ plist is list of turtles
    l is length of branch
    a is half of the angle between 2 branches
    f is factor by which branch is shortened
    from level to level.
    """
    for p in p列表:
        p.前進(l)
    if l > 5:
        列表 = []
        for p in p列表:
            q = p.複製()
            p.左轉(a)
            q.右轉(a)
            列表.append(p)
            列表.append(q)
        樹(列表, l*f, a, f)
    
def 製造樹():
    p = 龜類(shape="triangle", visible=假)
    p.設回復暫存區(無)
    p.填色(綠)
    p.形狀大小(0.4)
    p.速度(0)
    p.左轉(90)
    p.提筆()
    p.後退(210)
    p.下筆()
    樹([p], 200, 65, 0.6375)

def 主函數():
    幕.追蹤(30,0)
    a=clock()
    製造樹()
    b=clock()
    幕.追蹤(真)
    for t in 幕.龜群():
        t.顯龜()
    印(len(幕.龜群()))
    return "done: {0:.2f} sec.".format(b-a)

if __name__ == "__main__":
    訊息 = 主函數()
    印(訊息)
    幕.主迴圈()
