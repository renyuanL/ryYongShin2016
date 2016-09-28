#!/usr/bin/python
"""        turtle-example-suite:

            tdemo_planet.py

Gravitational system simulation using the
approximation method from Feynman-lectures,
Vol. 1, p.9-8, using turtlegraphics.

Example: heavy central body, light planet,
Note the (small) movement of the sun!

Demonstrates two features of the turtle module:
(1) use of "compound turtle shapes"-
planets consist of two semicircles of
different colour.
(2) Vec2D class (derived from tuple) allows
for a very concise formulation of the orbit
calculation algorithm. (Note that methods
like pos() return vectors.)
"""
from turtle_tc import *; from turtle_tc import 幕類, 龜類, 形狀類, 向量類

G常數 = 8

class 重力系統類(object):
    def __init__(我):
        我.行星們 = []
        我.dt = 0.01
    def 起始化(我):
        for p in 我.行星們:
            p.起始化()
    def 開始(我):
        for i in 範圍(10000):
            for p in 我.行星們:
                p.步進()
            幕類().更新()
            
class 星類(龜類):
    def __init__(我, m, x, v, 重力系統, 形狀):
        龜類.__init__(我, 形狀)
        我.重設大小模式("user")
        重力系統.行星們.append(我)
        我.重力系統 = 重力系統
        我.dt = 我.重力系統.dt
        我.提筆()
        我.m = m
        我.設位置(x)
        我.vel = v
        我.下筆()
    def 起始化(我):
        我.vel = 我.vel + 0.5*我.dt*我.加速度()
    def 加速度(我):
        a = 向量類(0,0)
        for 行星 in 我.重力系統.行星們:
            if 行星 != 我:
                r = 行星.位置()-我.位置()
                a += (G常數*行星.m/abs(r)**3)*r
        return a
    def 步進(我):
        我.設位置(我.位置() + 我.dt*我.vel)
        if 我 != 日:
            我.設頭向(我.朝向(日))
        我.vel = 我.vel + 我.dt*我.加速度()

## create compound yellow/blue turtleshape for planets
## yellow semicircle will point towards the sun
def createPlanetShape():
    s = 幕類()
    s.追蹤(0,0)
    t = 龜類()
    t.藏龜()
    t.提筆()
    t.前進(6)
    t.左轉(90)
    t.開始多邊形()
    t.畫圓(6, 180)
    t.結束多邊形()
    m1 = t.取多邊形()
    t.開始多邊形()
    t.畫圓(6,180)
    t.結束多邊形()
    m2 = t.取多邊形()

    行星形狀 = 形狀類("compound")
    行星形狀.加成員(m1,橙)
    行星形狀.加成員(m2,藍)
    s.登記形狀("planet", 行星形狀)
    s.追蹤(真,0)
    

def 主函數():
    global 日
    createPlanetShape()
    ## setup gravitational system
    gs = 重力系統類()
    日 = 星類(1000000, 向量類(50,0), 向量類(0,-3.5), gs, "circle")
    日.顏色(黃)
    日.龜大小(1.8)
    日.提筆()
    地球 = 星類(10000, 向量類(150,0), 向量類(0,350), gs, "planet")
    地球.筆色(綠)
    幕類().追蹤(假)
    gs.起始化()
    gs.開始()
    return "Done!"

if __name__ == '__main__':
    訊息 = 主函數()
    印(訊息)
    幕類().主迴圈()

