#!/usr/bin/python
"""       turtle-example-suite:

         tdemo_minimal_hanoi.py

A minimal 'Towers of Hanoi' animation:
A tower of 6 discs is transferred from the
left to the right peg.

An imho quite elegant and concise
implementation using a tower class, which
is derived from the built-in type list.

Discs are turtles with shape "square", but
stretched to rectangles by shapesize()
 ---------------------------------------
       To exit press STOP button
 ---------------------------------------
"""
from turtle_tc import *

class 盤類(龜類):
    def __init__(我, n):
        龜類.__init__(我, shape=方形, visible=假)
        我.提筆()
        我.形狀大小(1.5, n*1.5, 2) # square-->rectangle
        我.填色(n/6., 0, 1-n/6.)
        我.顯龜()

class 塔類(list):
    "Hanoi tower, a subclass of built-in type list"
    def __init__(我, x):
        "create an empty tower. x is x-position of peg"
        我.x = x
    def push(我, d):
        d.設x座標(我.x)
        d.設y座標(-150+34*len(我))
        我.append(d)
    def pop(我):
        d = list.pop(我)
        d.設y座標(150)
        return d

def 河內(n, 從_, 伴隨_, 去_):
    if n > 0:
        河內(n-1, 從_, 去_, 伴隨_)
        去_.push(從_.pop())
        河內(n-1, 伴隨_, 從_, 去_)

def 玩():
    在按鍵時(無,空白鍵)
    清除()
    河內(6, t1, t2, t3)
    寫("press STOP button to exit",
          align="center", font=("Courier", 16, "bold"))

def 主函數():
    global t1, t2, t3
    藏龜(); 提筆(); 前往(0, -225)   # writer turtle
    t1 = 塔類(-250)
    t2 = 塔類(0)
    t3 = 塔類(250)
    # make tower of 6 discs
    for i in 範圍(6,0,-1):
        t1.push(盤類(i))
    # prepare spartanic user interface ;-)
    寫("press spacebar to start game",
          align="center", font=("Courier", 16, "bold"))
    在按鍵時(玩, 空白鍵)
    聽()
    return "EVENTLOOP"

if __name__=="__main__":
    訊息 = 主函數()
    印(訊息)
    主迴圈()
