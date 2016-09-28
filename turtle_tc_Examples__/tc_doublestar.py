#!/usr/bin/python
"""       turtle-example-suite:

           tdemo_doublestar.py

Gravitational system simulation using the
approximation method from Feynman-lectures,
Vol. 1, p.9-8, using turtlegraphics

Example: heavy bodies of equal mass, moving
around the center of mass of the system.

"""
from turtle_tc import *; from turtle_tc import 龜類, 幕類, 向量類 
from time import sleep

G常數 = 8

class 重力系統類(object):
    def __init__(我):
        我.行星們 = []
        我.dt = 0.002
    def 起始化(我):
        for p in 我.行星們:
            p.起始化()
    def 開始(我):
        for i in 範圍(50000):
            for p in 我.行星們:
                p.步進()
            if i % 10 == 0:
                幕類().更新()
            
class 星類(龜類):
    def __init__(我, m, x, v, 重力系統, 形狀):
        龜類.__init__(我, 形狀)
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
        我.v = 我.v + dt*我.加速度()

def 主函數():
    ## setup gravitational system
    gs = 重力系統類()
    sun1 = 星類(400000, 向量類(-150,0), 向量類(0,-80), gs, "circle")
    sun1.顏色(紅)
    sun2 = 星類(400000, 向量類(150,0), 向量類(0,80), gs, "circle")
    sun2.顏色(橙)
    幕類().追蹤(假)
    gs.起始化()
    gs.開始()

if __name__ == '__main__':
    主函數()
    幕類().主迴圈()

