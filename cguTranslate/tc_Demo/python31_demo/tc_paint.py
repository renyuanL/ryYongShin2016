#!/usr/bin/python
"""       turtle-example-suite:

            tdemo_paint.py

A simple  eventdriven paint program

- use left mouse button to move turtle
- middle mouse button to change color
- right mouse button do turn filling on/off
 -------------------------------------------
 Play around by clicking into the canvas
 using all three mouse buttons.
 -------------------------------------------
          To exit press STOP button
 -------------------------------------------
"""
from turtle_tc import *

def 切換提筆下筆(x=0, y=0):
    if 筆()["pendown"]:
        結束填()
        提筆()
    else:
        下筆()
        開始填()

def 改變顏色(x=0, y=0):
    global 顏色們
    顏色們 = 顏色們[1:]+顏色們[:1]
    顏色(顏色們[0])

def 主函數():
    global 顏色們
    形狀("circle")
    重設大小模式("user")
    形狀大小(.5)
    筆寬(3)
    顏色們=[紅, 綠, 藍, 黃]
    顏色(顏色們[0])
    切換提筆下筆()
    在點擊幕時(前往,1)
    在點擊幕時(改變顏色,2)
    在點擊幕時(切換提筆下筆,3)
    return "EVENTLOOP"

if __name__ == "__main__":
    訊息 = 主函數()
    印(訊息)
    主迴圈()
