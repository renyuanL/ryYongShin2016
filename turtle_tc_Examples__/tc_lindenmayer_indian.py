#!/usr/bin/python
"""       turtle-example-suite:

        xtx_lindenmayer_indian.py

Each morning women in Tamil Nadu, in southern
India, place designs, created by using rice
flour and known as kolam on the thresholds of
their homes.

These can be described by Lindenmayer systems,
which can easily be implemented with turtle
graphics and Python.

Two examples are shown here:
(1) the snake kolam
(2) anklets of Krishna

Taken from Marcia Ascher: Mathematics
Elsewhere, An Exploration of Ideas Across
Cultures

"""
################################
# Mini Lindenmayer tool
###############################

from turtle_tc import *

def replace( 序列, 取代規則們, n ):
    for i in 範圍(n):
        新序列 = ""
        for 元素 in 序列:
            新序列 = 新序列 + 取代規則們.get(元素,元素)
        序列 = 新序列
    return 序列

def 畫( 指令們, 規則們 ):
    for b in 指令們:
        try:
            規則們[b]()
        except TypeError:
            try:
                畫(規則們[b], 規則們)
            except:
                pass


def 主函數():
    ################################
    # Example 1: Snake kolam
    ################################


    def r():
        右轉(45)

    def l():
        左轉(45)

    def f():
        前進(7.5)

    蛇規則 = {"-":r, "+":l, "f":f, "b":"f+f+f--f--f+f+f"}
    蛇取代規則們 = {"b": "b+f+b--f--b+f+b"}
    蛇開始 = "b--f--b--f"

    正在畫 = replace(蛇開始, 蛇取代規則們, 3)

    重設()
    速度(3)
    追蹤(1,0)
    藏龜()
    提筆()
    後退(195)
    下筆()
    畫(正在畫, 蛇規則)

    from time import sleep
    sleep(3)

    ################################
    # Example 2: Anklets of Krishna
    ################################

    def A():
        顏色(紅)
        畫圓(10,90)

    def B():
        from math import sqrt
        顏色(黑)
        l = 5/sqrt(2)
        前進(l)
        畫圓(l, 270)
        前進(l)

    def F():
        顏色(綠)
        前進(10)

    克里希納規則們 = {"a":A, "b":B, "f":F}
    克里希納取代規則們 = {"a" : "afbfa", "b" : "afbfbfbfa" }
    克里希納開始 = "fbfbfbfb"

    重設()
    速度(0)
    追蹤(3,0)
    藏龜()
    左轉(45)
    正在畫 = replace(克里希納開始, 克里希納取代規則們, 3)
    畫(正在畫, 克里希納規則們)
    追蹤(1)
    return "Done!"

if __name__=='__main__':
    訊息 = 主函數()
    印(訊息)
    主迴圈()
