"""       turtle-example-suite:

            tdemo_chaos.py
      "Don't trust your computer!" 

Plotting the graphs of the iteration of three
mathemtically identical functions.
(Verhulst dynamics) They show (1) chaotic and
(2) profoundly diverging behaviour.
"""
from turtle_tc import *

N = 80

def f(x):
    return 3.9*x*(1-x)

def g(x):
    return 3.9*(x-x**2)

def h(x):
    return 3.9*x-3.9*x*x

def 跳至(x, y):
    提筆(); 前往(x,y)

def 直線(x1, y1, x2, y2):
    跳至(x1, y1)
    下筆()
    前往(x2, y2)

def 座標系統():
    直線(-1, 0, N+1, 0)
    直線(0, -0.1, 0, 1.1)

def 畫(函數, 開始, colour):
    筆色(colour)
    x = 開始
    跳至(0, x)
    下筆()
    點(5)
    for i in 範圍(N):
        x=函數(x)
        前往(i+1,x)
        點(5)

def 主函數():
    重設()
    設座標系統(-1.0,-0.1, N+1, 1.1)
    速度(0)
    藏龜()
    座標系統()
    畫(f, 0.35, 藍)
    畫(g, 0.35, 綠)
    畫(h, 0.35, 紅)
    # Now zoom in:
    for s in 範圍(100):
        設座標系統(0.5*s,-0.1, N+1, 1.1)
    return "Done!"

if __name__ == "__main__":
    主函數()
    主迴圈()
