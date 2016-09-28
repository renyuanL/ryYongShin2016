"""       turtle-example-suite:

           tdemo_illusion_5.py

This script uses more advanced features
of the turtle module: Compound shapes,
that are sheared and tilted. (Naturally
a simpler solution using elemtary turtle
graphics commands only is possible.)

Circles of diamonds seem to rotate
if you focus your eyes on their center.

Inspired by NetLogo's model of optical
illusions.
"""
from turtle_tc import *

def 主函數():
    diamondshape = 形狀類("compound")
    poly1 = ((-7,-7), (7,-7), (7,7), (7,-7))
    diamondshape.加成員(poly1, 黑)
    poly2 = ((-7,-7), (-7,7), (7,7), (-7,7))
    diamondshape.加成員(poly2, 白)
    登記形狀("diamond", diamondshape)

    背景色("gray55")
    形狀("diamond")
    扭曲因子(0.3)
    提筆()
    藏龜()

    追蹤(假)
    左轉(90)
    for _ in 範圍(40):
        前進(160)
        蓋章()
        後退(160)
        右轉(9)
    傾斜(-73.3)
    for _ in 範圍(32):
        前進(125)
        蓋章()
        後退(125)
        右轉(11.25)
    點(12)

    前往(0, -270)
    寫("Stare at the dot, "
          "then lean forward and back!",
          align="center",
          font=("Courier",14,"bold"))
    追蹤(真)
    return "DONE!"

if __name__ == "__main__":
    訊息 = 主函數()
    印(訊息)
    主迴圈()
