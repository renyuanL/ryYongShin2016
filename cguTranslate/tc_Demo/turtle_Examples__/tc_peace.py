#!/usr/bin/python
"""       turtle-example-suite:

              tdemo_peace.py

A very simple drawing suitable as a beginner's
programming example.

Uses only commands, which are also available in
old turtle.py.

Intentionally no variables are used except for the
colorloop:
"""

from turtle_tc import *

def 主函數():
    和平顏色們 = ("red3",  橙, 黃,
                   "seagreen4", "orchid4",
                   "royalblue1", "dodgerblue4")

    重設()
    s = 幕類()
    提筆()
    前往(-320,-195)
    筆寬(70)

    for p顏色 in 和平顏色們:
        顏色(p顏色)
        下筆()
        前進(640)
        提筆()
        後退(640)
        左轉(90)
        前進(66)
        右轉(90)

    筆寬(25)
    顏色(白)
    前往(0,-170)
    下筆()

    畫圓(170)
    左轉(90)
    前進(340)
    提筆()
    左轉(180)
    前進(170)
    右轉(45)
    下筆()
    前進(170)
    提筆()
    後退(170)
    左轉(90)
    下筆()
    前進(170)
    提筆()

    前往(0,300) # vanish if hideturtle() is not available ;-)
    return "Done!!"

if __name__ == "__main__":
    主函數()
    主迴圈()
