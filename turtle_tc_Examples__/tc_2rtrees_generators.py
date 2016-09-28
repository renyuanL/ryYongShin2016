#!/usr/bin/python
"""      turtle-example-suite:

             tdemo_tree.py

Displays a 'breadth-first-tree' - in contrast
to the classical Logo tree drawing programs,
which use a depth-first-algorithm.

Uses:
(1) Turtle-cloning: At each branching point the
current turtle is cloned. 
(2) a tree-generator, where the drawing is
quasi the side-effect, whereas the generator
always yields None. This allows for drawing
trees in parallel - sort of 'micro-threads'.

See: tdemo_2rtrees_generators.py
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
        yield p.前進(l)
    if l > 4:
        列表 = []
        for p in p列表:
            q = p.複製()
            p.左轉(a)
            q.右轉(a)
            列表.append(p)
            列表.append(q)
        for x in 樹(列表, l*f, a, f):
            yield 無
    
def 製造樹(x):
    p = 龜類(shape="triangle", visible=假)
    p.設回復暫存區(無)
    p.填色(綠)
    p.形狀大小(0.4)
    p.速度(0)
    p.左轉(90)
    p.提筆()
    p.前往(x, -110)
    p.下筆()
    return 樹([p], 140, 65, 0.6375)

def 主函數():
    幕.追蹤(1, 0)
    a=clock()
    t1 = 製造樹(-206)
    t2 = 製造樹(206)
    while 真:
        做完了 = 0
        for t in t1, t2:
            try:
                next(t)
            except:
                做完了 += 1
        if 做完了 == 2:
            break
    幕.追蹤(真)
    b=clock()
    return "done: {0:.2f} sec.".format(b-a)

if __name__ == "__main__":
    訊息 = 主函數()
    印(訊息)
    幕.主迴圈()
