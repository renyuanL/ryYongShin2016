#!/usr/bin/python
"""       turtle-example-suite:

            tdemo_clock.py

Simple demonstration of 2 features of
xturtle:

(1) using a user defined turtle shape, namely
the clock's hand (lines 21-33, 49-54)
(2) animation via ontimer (l. 56-61)

After drawing the clock-face and the hand
the program enters the EVENTLOOP. Only
Timer events are registered.

   Press STOP to exit the program!
   ===============================
"""

from turtle_tc import *

def 主函數():
    重設()
    左轉(90)

    開始多邊形()
    前進(100)
    右轉(90)
    前進(10)
    左轉(120)
    前進(20)
    左轉(120)
    前進(20)
    左轉(120)
    前進(10)
    結束多邊形()    

    指針 = 取多邊形()

    左轉(90)
    後退(100)
    清除()
    筆粗(7)

    提筆()
    for i in 範圍(12):
        前進(125)
        下筆()
        前進(25)
        提筆()
        後退(150)
        右轉(30)
        
    登記形狀("hand", 指針)
    形狀("hand")
    重設大小模式("user")
    龜大小(1, 1, 3)
    顏色(紅, 藍)

    def 滴答():
        右轉(6)
        在計時後(滴答, 1000)

    速度(1)
    在計時後(滴答, 1000)
    return "EVENTLOOP"

if __name__ == '__main__':
    主函數()
    主迴圈()    



    
