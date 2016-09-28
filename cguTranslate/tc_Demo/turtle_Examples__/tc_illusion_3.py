"""       turtle-example-suite:

           tdemo_illusion_3.py

A simple drawing suitable as a beginner's
programming example.

This version makes the turtle have a
rectangular shape and uses the stamp()
command to draw rectangles.

The perpendicular lines that do not match
row to row create an illusion of the lines
between them being not parallel.

Inspired by NetLogo's model of optical
illusions.
"""

from turtle_tc import *

def 主函數():
    背景色("gray60")

    提筆()
    速度(0)
    藏龜()
    形狀(方形)
    形狀大小(3.2, 3.5)

    平移 = [10, 0, 10, 28,
             10, 0, 10, 28, 10]

    追蹤(假)
    for i in 範圍(9):
        前往(-365 + 平移[i], 267-66*i)
        顏色(黑)
        for i in 範圍(11):
            蓋章()
            前進(70)
            if 筆色() == 白:
                顏色(黑)
            else:
                顏色(白)
    追蹤(真)
    return "DONE!"

if __name__ == "__main__":
    訊息 = 主函數()
    印(訊息)
    主迴圈()


