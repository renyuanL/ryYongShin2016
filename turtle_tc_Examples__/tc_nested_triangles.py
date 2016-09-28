"""       turtle-example-suite:

        tdemo_nested triangles.py

This script demonstrates how to use the
turtle as a 'land surveyor', i. e.
how to determine distances and angles
without trigonometical calculations.

Sort of preliminary study to round_dance.
"""
from turtle_tc import *
import time

def 主函數():
    模式(角度從北開始順時針)
    形狀("triangle")

    # determine shriking factor
    # and angle of rotation
    速度(1)
    前進(100)
    右轉(150)
    前進(20)
    設頭向(朝向(0,0))
    右轉(180)
    # now the turtle is at the tip of 
    # the inscribed triangle with heading
    # in direction of its axis.
    f = 距離(0,0)/100  # 0.83282...
    φ = 頭向()        # 6.89636...
    time.sleep(1)

    # go home
    後退(100*f)
    左轉(φ)
    time.sleep(1)

    # stamp nested triangles
    清除()
    s = 20
    c = 1
    for i in 範圍(20):
        形狀大小(s)
        填色(c, 0.5, 1-c)
        蓋章()
        s *= f
        c *= f
        右轉(φ)
    return "DONE!"

if __name__ == "__main__":
    訊息 = 主函數()
    印(訊息)
    主迴圈()   
