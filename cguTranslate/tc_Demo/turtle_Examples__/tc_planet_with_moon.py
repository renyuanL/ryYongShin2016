#!/usr/bin/python
"""       turtle-example-suite:

        tdemo_planet_with_moon.py

Gravitational system simulation using the
approximation method from Feynman-lectures,
Vol. 1, p.9-8, using turtlegraphics.

Example: heavy central body, light planet,
very light moon!
Planet has a circular orbit, moon a stable
orbit around the planet.

You can hold the movement temporarily by pressing
the left mouse button with mouse over the
scrollbar of the canvas.

"""
from turtle_tc import *; from turtle_tc import 形狀類, 龜類, 幕類, 向量類 as 向量類
from time import sleep

G常數 = 8

class 重力系統類(object):
    def __init__(我):
        我.行星們 = []
        我.t = 0
        我.dt = 0.01
    def 起始化(我):
        for p in 我.行星們:
            p.起始化()
    def 開始(我):
        for i in 範圍(10000):
            我.t += 我.dt
            for p in 我.行星們:
                p.步進()

class 星類(龜類):
    def __init__(我, m, x, v, 重力系統, 形狀):
        龜類.__init__(我, shape=形狀)
        我.提筆()
        我.m = m
        我.設位置(x)
        我.v = v
        重力系統.行星們.append(我)
        我.重力系統 = 重力系統
        我.重設大小模式("user")
        我.下筆()
    def 起始化(我):
        dt = 我.重力系統.dt
        我.a = 我.加速度()
        我.v = 我.v + 0.5*dt*我.a
    def 加速度(我):
        a = 向量類(0,0)
        for 行星 in 我.重力系統.行星們:
            if 行星 != 我:
                v = 行星.位置()-我.位置()
                a += (G常數*行星.m/abs(v)**3)*v
        return a
    def 步進(我):
        dt = 我.重力系統.dt
        我.設位置(我.位置() + dt*我.v)
        if 我.重力系統.行星們.index(我) != 0:
            我.設頭向(我.朝向(我.重力系統.行星們[0]))
        我.a = 我.加速度()
        我.v = 我.v + dt*我.a

## create compound yellow/blue turtleshape for planets

def 主函數():
    s = 龜類()
    s.重設()
    幕類().追蹤(0,0)
    s.藏龜()
    s.提筆()
    s.前進(6)
    s.左轉(90)
    s.開始多邊形()
    s.畫圓(6, 180)
    s.結束多邊形()
    m1 = s.取多邊形()
    s.開始多邊形()
    s.畫圓(6,180)
    s.結束多邊形()
    m2 = s.取多邊形()

    行星形狀 = 形狀類("compound")
    行星形狀.加成員(m1,橙)
    行星形狀.加成員(m2,藍)
    s.取幕().登記形狀("planet", 行星形狀)
    幕類().追蹤(1,0)

    ## setup gravitational system
    gs = 重力系統類()
    日 = 星類(1000000, 向量類(0,0), 向量類(0,-2.5), gs, "circle")
    日.顏色(黃)
    日.形狀大小(1.8)
    日.提筆()
    地球 = 星類(12500, 向量類(210,0), 向量類(0,195), gs, "planet")
    地球.筆色(綠)
    地球.形狀大小(0.8)
    月球 = 星類(1, 向量類(220,0), 向量類(0,295), gs, "planet")
    月球.筆色(藍)
    月球.形狀大小(0.5)
    gs.起始化()
    gs.開始()
    return "Done!"

if __name__ == '__main__':
    訊息 = 主函數()
    印(訊息)
    幕類().主迴圈()
