"""       turtle-example-suite:

           tdemo_graviturtle.py

Very simple prototype of a gravitational
system consisting of a central body and
an orbiting turtle.

Demonstrates specifically the use of the
Vec2D class and corresponding properties
of turtles for doing vector calculations.

An only little more sophisticated approach
is used by the other gravitation examples.
"""
from turtle_tc import *

def 主函數():
    顏色(橙)
    點(10)
    center = 位置()
    顏色(藍)
    形狀(龜形)
    速度(0)
    提筆(); 前往(200,0); 下筆()

    G常數 = 800
    v = 向量類(0, 1)
    t = 0
    dt = 1
    while t < 1100:
        前往(位置() + v*dt)
        設頭向(朝向(center))
        r = 距離(center)
        加速度 = (-G常數/r**3)*位置()
        v = v + 加速度*dt
        t = t + dt
    return "DONE!"

if __name__ == "__main__":
    訊息 = 主函數()
    印(訊息)
    主迴圈()   
    
    
    
        
