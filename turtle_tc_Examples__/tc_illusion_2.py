"""       turtle-example-suite:

           tdemo_illusion_2.py

A simple drawing suitable as a beginner's
programming example.

Diagonals moving away from the center create
an illusion of depth, which makes the parallel
horizontal lines seem to bend in the center.

Inspired by NetLogo's model of optical
illusions.
"""
from turtle_tc import *

def 主函數():
    追蹤(假)
    藏龜()
    速度(0)
    筆粗(2)
    左轉(90)
    for i in 範圍(30):
        提筆()
        後退(500)
        下筆()
        前進(1000)
        提筆()
        後退(500)
        左轉(6)
    點(60)

    筆粗(16)
    前進(53)
    右轉(90)
    後退(400)
    下筆()
    前進(800)
    提筆()
    後退(400)
    左轉(90)
    後退(106)
    右轉(90)
    後退(400)
    下筆()
    前進(800)
    提筆()
    後退(400)
    左轉(90)
    前進(330)
    筆色(紅)
    寫("Are the thick lines parallel?",
          align="center",
          font=("Courier",24,"bold"))
    追蹤(真)
    return "DONE!"

if __name__ == "__main__":
    訊息 = 主函數()
    印(訊息)
    主迴圈()
