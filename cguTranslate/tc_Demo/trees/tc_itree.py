"""      turtle-example-suite:

            tdemo_itree.py

Displays a 'breadth-first-tree' - in contrast
to the classical Logo tree drawing programs,
which use a depth-first-algorithm.

Uses turtle-cloning: At each branching point
the current turtle is cloned.

Branching depth is visualized by colors.

As the recursive breadth first tree scripts
are tail recursive they can easily be
transformed into iterative versions.
This is an example.
"""

from turtle_tc import *; from turtle_tc import 幕類, 龜類

幕 = 幕類()

def itree(t, l, f, 顏色們):
    t.顏色(顏色們[0])
    t.前進(l)
    龜群 = [t]
    顏色們.pop(0)
    while 顏色們:
        l *= f
        newturtles = []
        for t in 龜群:
            t.顏色(顏色們[0])
            t1 = t.複製()
            t.左轉(45)
            t.前進(l)
            t1.右轉(45)
            t1.前進(l)
            newturtles.extend([t, t1])
        龜群 = newturtles
        顏色們.pop(0)
    for t in 龜群:
        t.顏色(綠)
            
def 主函數():
    幕.模式(角度從北開始順時針)
    t = 龜類(shape="triangle")
    t.提筆(); t.後退(280); t.下筆()
    t.筆粗(3)
    itree(t, 250, 0.63,
          [黑, "brown", 紅, 橙, "violet", "lightblue"])

if __name__ == '__main__':
    主函數()
    幕.主迴圈()
