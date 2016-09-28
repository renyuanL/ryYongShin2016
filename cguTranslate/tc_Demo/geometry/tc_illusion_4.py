"""       turtle-example-suite:

           tdemo_illusion_4.py

A simple drawing suitable as a beginner's
programming example.

Relative sizes of other circles skew the
perception of the middle circles, creating
an illusion of difference in size.

Inspired by NetLogo's model of optical
illusions.
"""

from turtle_tc import *


def circlepattern(r1, d, r2):
    點(2*r1)
    左轉(30)
    R = r1 + d + r2
    for i in 範圍(6):
        前進(R)
        點(2*r2)
        後退(R)
        左轉(60)
    右轉(30)

def 主函數():
    背景色(黑)
    藏龜()
    提筆()
    顏色(白)

    追蹤(假)
    後退(200)
    circlepattern(36, 3, 16)
    前進(300)
    circlepattern(36, 20, 56)

    前往(0, -270)
    筆色(白)
    寫("Which inner circle is bigger?",
          align="center",
          font=("Courier",14,"bold"))
    追蹤(真)

    return "DONE!"

if __name__ == '__main__':
    訊息 = 主函數()
    印(訊息)
    主迴圈()    
