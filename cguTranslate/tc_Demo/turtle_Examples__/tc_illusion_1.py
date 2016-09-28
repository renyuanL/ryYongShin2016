"""       turtle-example-suite:

           tdemo_illusion_1.py

A simple drawing suitable as a beginner's
programming example.

This script uses user defined coordinates
in a way that the intersection points of
the lines have integer coordinates. 
Stamps squares and circles.

White circles on a gray background produce
an illusion of the circles changing colors
between black and white, depending on
where you focus your eyes.

Inspired by NetLogo's model of optical
illusions.
"""

from turtle_tc import *

def 主函數():
    設立(800, 600)
    背景色("gray60")
    設座標系統(-4.4, -3.3, 4.4, 3.3)
    藏龜()
    提筆()
    追蹤(假)
    顏色(黑)
    形狀(方形)
    形狀大小(3.4)
    for 行 in 範圍(-5, 5):
        for 列 in 範圍(-4, 4):
            前往(行+0.5, 列+0.5)
            蓋章()
    顏色(白)
    形狀("circle")
    形狀大小(1.6)
    for 行 in 範圍(-5, 5):
        for 列 in 範圍(-4, 4):
            前往(行, 列)
            蓋章()
    追蹤(真)
    return "DONE!"

if __name__ == "__main__":
    訊息 = 主函數()
    印(訊息)
    主迴圈()
    
