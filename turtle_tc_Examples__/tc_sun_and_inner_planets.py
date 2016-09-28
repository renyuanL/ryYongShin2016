#!/usr/bin/python
"""        turtle-example-suite:

      tdemo_sun_and_inner_planets.py

Gravitational system simulation using the
approximation method from Feynman-lectures,
Vol.1, p.9-8, using turtlegraphics

This example uses real phyisical data of
our planetary system: simulates the four
inner planets orbiting around the sun.

Demonstrates the use of (user defined)
worldcoordinates.
"""
from turtle_tc import *; from turtle_tc import 幕類, 龜類, 形狀類, 向量類

AE = 1.5e11
# masses
mS = 2.e30
mE = 6.e24
mME = 3.3e23
mVE = 4.869e24
mMA = 6.419e23

G常數 = 6.67e-11
# radii of the orbits
rE = 1.5e11
perihelME = .307*AE  # orbit is fairly eccentric
rVE = 0.732*AE
rMA = 1.524*AE
# velocities
vE = 3.e4
perihelvME = 5.9e4
vVE = 3.502e4
vMA = 2.413e4
DT = 10800
# half width of user coordinate system (in meters)
hfw =  2.5e11 

class 重力系統類(object):
    def __init__(我):
        我.行星們 = []
        我.dt = DT
    def 起始化(我):
        for p in 我.行星們:
            p.起始化()
    def 開始(我):
        s.追蹤(假)
        for i in 範圍(10000):
            for p in 我.行星們:
                p.步進()
            s.更新()
            
class 星類(龜類):
    def __init__(我, m, x, v, 重力系統, 形狀):
        龜類.__init__(我, 形狀)
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
    global s, 日
    s = 幕類()
    s.設立(800, 600, 50, 50)
    s.幕大小(750, 550)
    createPlanetShape()
    ## setup gravitational system
    s.設座標系統(-hfw*4/3, -hfw, hfw*4/3, hfw)
    gs = 重力系統類()
    日 = 星類(mS, 向量類(0.,0.), 向量類(0.,0.), gs, "circle")
    日.顏色(黃)
    日.龜大小(1.8)
    日.提筆()
    地球 = 星類(mE, 向量類(rE,0.), 向量類(0.,vE), gs, "planet")
    地球.筆色(綠)
    地球.形狀大小(0.8)
    mercury = 星類(mME, 向量類(0., perihelME), 向量類(-perihelvME, 0),
                                                        gs, "planet")
    mercury.筆色(藍)
    mercury.形狀大小(0.5)
    venus = 星類(mVE, 向量類(-rVE, 0.), 向量類(0., -vVE), gs, "planet")
    venus.筆色(藍)
    venus.形狀大小(0.65)
    mars = 星類(mMA, 向量類(0., -rMA), 向量類(vMA, 0.), gs, "planet")
    mars.筆色(藍)
    mars.形狀大小(0.45)
    gs.起始化()
    gs.開始()
    return "Done!"

if __name__ == '__main__':
    訊息 = 主函數()
    印(訊息)
    幕類().主迴圈()

