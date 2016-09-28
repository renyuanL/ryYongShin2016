#!/usr/bin/python
"""       turtle-example-suite:

            tdemo_plants.py

Lindenmayer systems, named after the biologist
Aristid Lindenmayer, are formal grammars used
to model the growth of plants and many more
patterns (see example indianDesigns).

For more information see:
http://en.wikipedia.org/wiki/Lindenmayer_system

Here are two examples produced in parallel by
Lindenmayer generators

"""
####################################
# Mini Lindenmayer tool -
# this time a bit more sophisticated
####################################

from turtle_tc import *; from turtle_tc import 龜類, 幕類

def replace( 序列, 取代規則們, n ):
    for i in 範圍(n):
        新序列 = ""
        for 元素 in 序列:
            新序列 += 取代規則們.get(元素,元素)
        序列 = 新序列  
    return 序列

def lindenmayer(turtle,
                axiom = "",
                取代規則們 = {},
                深度 = 1,
                步進 = 5,
                角度 = 90,
                開始位置 = (0,-120),
                startdir = 90,
                updating = 20):
    turtle.步進, turtle.角度 = 步進, 角度
    正在畫 = replace(axiom, 取代規則們, 深度)
    幕類().追蹤(updating)
    turtle.開始(開始位置, startdir)
    return turtle.畫(正在畫, turtle.standardRules()) 
    

class LPen(龜類):
    def __init__(我):
        龜類.__init__(我)
        我.速度(0)
        我.藏龜()
        我.tstack = []
        
    def 開始(我, 開始位置, startdir):
        我.提筆()
        我.前往(開始位置)
        我.左轉(startdir)
        我.下筆()

    def 畫( 我, 指令們, 規則們):
        i = 0
        for c in 指令們:
            try:
                規則們[c]()
            except:
                pass
            # We turn it into a generator!                
            yield 1

    ################################
    # Standardrules
    ################################

    def r(我):
        我.右轉(我.角度)

    def l(我):
        我.左轉(我.角度)

    def f(我):
        我.提筆()
        我.前進(我.步進)

    def F(我):
        我.下筆()
        我.前進(我.步進)

    def turn(我):
        我.左轉(180)

    def save(我):
        我.tstack.append( (我.位置(), 我.頭向()) )

    def load(我):
        位置, richtung = 我.tstack.pop()
        我.提筆()
        我.前往(位置)
        我.設頭向(richtung)

    def standardRules(我):
        return {"-":我.l, "+":我.r, "F": 我.F, "f":我.f,
                "|": 我.turn, "[":我.save, "]":我.load}

# 2 examples for Lindenmayer plants:
herb = {
         "axiom" : "G",
         "取代規則們" : { "G" : "GFX[+G][-G]",
                                "X" : "X[-FFF][+FFF]FX" },
         "深度" : 5,
         "步進" : 6.75,
         "角度" : 180.0/7,
         "開始位置" : (-135, -192),
         "startdir" : 90
       }

bush = {
         "axiom" : "F",
         "取代規則們" : { "F" : "FF+[+F-F-F]-[-F+F+F]" },
         "深度" : 3,
         "步進" : 13.5,
         "角度" : 180.0/8,
         "開始位置" : (90, -192),
         "startdir" : 90,
       }


def 主函數():
    l1 = lindenmayer(LPen(), **herb)
    l2 = lindenmayer(LPen(), **bush)
    做完了 = 0
    while 做完了 < 2:
        做完了 = 0
        for l in l1, l2:
            try:
                next(l)
            except StopIteration:
                做完了 += 1
    幕類().追蹤(真)
    return "Done!"
    

if __name__ == '__main__':
    訊息 = 主函數()
    印(訊息)
    幕類().主迴圈()
