#!/usr/bin/python
"""       turtle-example-suite:

     tdemo-I_dont_like_tiltdemo.py

Demostrates
  (a) use of a tilted ellipse as
      turtle shape
  (b) stamping that shape

We can remove it, if you don't like it.
      Without using reset() ;-)
 ---------------------------------------
"""
from turtle_tc import *
import time

def 主函數():
    重設()
    形狀("circle")
    重設大小模式("user")

    提筆(); 後退(24*18/6.283); 右轉(90); 下筆()
    傾斜(45)

    提筆()

    龜大小(16,10,5)
    顏色(紅, "violet")
    for i in 範圍(18):
        前進(24)
        左轉(20)
        蓋章()
    顏色(紅, "")
    for i in 範圍(18):
        前進(24)
        左轉(20)
        蓋章()

    傾斜(-15)
    龜大小(3, 1, 4)
    顏色(藍, 黃)
    for i in 範圍(17):
        前進(24)
        左轉(20)
        if i%2 == 0:
            蓋章()
    time.sleep(1)
    while 回復暫存區的個數():
        回復()
    藏龜()
    寫("OK, OVER!", align="center", font=("Courier", 18, "bold"))
    return "Done!"

if __name__=="__main__":
    訊息 = 主函數()
    印(訊息)
#    mainloop()
