#!/usr/bin/python
"""     turtlegraphics-example-suite:

             tdemo_forest.py

Displays a 'forest' of 3 'breadth-first-trees'
similar to the one from example tree.
For further remarks see xtx_tree.py

This example is a 'breadth-first'-rewrite of
a Logo program written by Erich Neuwirth. See:
http://homepage.univie.ac.at/erich.neuwirth/
"""
from turtle_tc import *; from turtle_tc import 龜類, 幕類
from random import randrange
from time import clock

def 隨機符號(n):
    return randrange(-n,n+1)

def 隨機化( 分支列表, 角度距離, 邊距離 ):
    return [ (角度+隨機符號(角度距離),
              尺寸因子*1.01**隨機符號(邊距離))
                     for 角度, 尺寸因子 in 分支列表 ]

def 隨機前進( t, 距離, 部分, 角度距離 ):
    for i in 範圍(部分):
        t.左轉(隨機符號(角度距離))
        t.前進( (1.0 * 距離)/部分 )

def 樹(t列表, 尺寸, 等級, 寬度因子, 分支列表們, 角度距離=10, 邊距離=5):
    # benutzt Liste von turtles und Liste von Zweiglisten,
    # fuer jede turtle eine!
    if 等級 > 0:
        列表 = []
        brs = []
        for t, 分支列表 in list(zip(t列表,分支列表們)):
            t.筆粗( 尺寸 * 寬度因子 )
            t.筆色( 255 - (180 - 11 * 等級 + 隨機符號(15)),
                        180 - 11 * 等級 + 隨機符號(15),
                        0 )
            t.下筆()
            隨機前進(t, 尺寸, 等級, 角度距離 )
            yield 1
            for 角度, 尺寸因子 in 分支列表:
                t.左轉(角度)
                列表.append(t.複製())
                brs.append(隨機化(分支列表, 角度距離, 邊距離))
                t.右轉(角度)
        for x in 樹(列表, 尺寸*尺寸因子, 等級-1, 寬度因子, brs,
                      角度距離, 邊距離):
            yield 無


def 開始(t,x,y):
    t.重設()
    t.速度(0)
    t.藏龜()
    t.左轉(90)
    t.提筆()
    t.設位置(x,y)
    t.下筆()

def 做它1(等級, 筆):
    筆.藏龜()
    開始(筆, -10, -218)
    t = 樹( [筆], 80, 等級, 0.1, [[ (45,0.69), (0,0.65), (-45,0.71) ]] )
    return t

def 做它2(等級, 筆):
    筆.藏龜()
    開始(筆, -135, -80)
    t = 樹( [筆], 120, 等級, 0.1, [[ (45,0.69), (-45,0.71) ]] )
    return t

def 做它3(等級, 筆):
    筆.藏龜()
    開始(筆, 190, -90)
    t = 樹( [筆], 100, 等級, 0.1, [[ (45,0.7), (0,0.72), (-45,0.65) ]] )
    return t

def doit4(等級, 筆):
    筆.藏龜()
    開始(筆, -270, -250)
    t = 樹( [筆], 60, 等級, 0.1, [[ (55,0.75), (0,0.73), (-35,0.62) ]] )
    return t

def doit5(等級, 筆):
    筆.藏龜()
    開始(筆, 265, -280)
    t = 樹( [筆], 100, 等級, 0.1, [[ (10,0.62), (5,0.80), (-10,0.72) ]] )
    return t

# Hier 3 Baumgeneratoren:
def 主函數():
    global 幕
    幕 = 幕類()
    幕.色模式(255)
    p = 龜類()
    p.藏龜()
    幕.追蹤(75,0)
    u = 做它1(6, 龜類(undobuffersize=1))
    s = 做它2(7, 龜類(undobuffersize=1))
    t = 做它3(5, 龜類(undobuffersize=1))
    v = doit4(6, 龜類(undobuffersize=1))
    w = doit5(5, 龜類(undobuffersize=1))
    a = clock()
    while 真:
        做完了 = 0
        for b in u,s,t,v,w:
            try:
                next(b)
            except:
                做完了 += 1
        if 做完了 == 5:
            break

    幕.追蹤(1,10)
    b = clock()
    return "runtime: {0:.2f} sec.".format(b-a)

if __name__ == '__main__':
    訊息 = 主函數()
    印(訊息)
    幕.主迴圈()
