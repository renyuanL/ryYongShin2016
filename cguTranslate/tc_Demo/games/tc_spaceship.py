#!/usr/bin/python
"""       turtle-example-suite:

           tdemo_spaceship.py

How does rocket propulsion work?
Play this game to learn about it.

The keys:

<space> starts a new game

Arrow-Keys:
<up> exerts a force (for a moment) and so
     accelerates spaceship in direction of
     its heading
<left>,<right> turns spaceship by 10 degrees

If the canvas has lost the focus, click into
it!

   Press STOP to exit the program!
   ===============================

Remark: this is a rather old script;
a rewrite possibly  on OOP basis
would make it clearer and/or cleaner.
"""
from turtle_tc import *
from time import clock

FORCE_UNIT = 0.1  # change this to fine-tune
                  # control of the spaceship
                  # on your machine

smallfont  = ("Courier", 12, "bold")
normalfont = ("Courier", 18, "normal")
boldfont   = ("Courier", 18, "bold")

def scenery():
    global target
    designer.藏龜()
    designer.速度(0)
    designer.提筆()
    designer.左轉(180)
    designer.前進(240)
    designer.左轉(90)
    designer.筆粗(10)
    designer.筆色(藍)
    designer.畫圓(120, 15)
    designer.下筆()
    designer.畫圓(120, 330)
    designer.提筆()
    designer.畫圓(120, 15)
    designer.左轉(90)
    designer.前進(120)
    designer.點(20, 黃)
    target = designer.位置()

# spaceship is the "anonymous" turtle
def 開始():
    global vx, vy
    vx, vy = 0.0, 0.0
    重設()
    藏龜()
    速度(0)
    筆粗(7)
    顏色(紅, 橙)
    提筆()
    前進(120)
    下筆()
    左轉(90)
    顯龜()
    # hint for the player
    寫手.重設()
    寫手.藏龜()
    寫手.速度(0)
    寫手.提筆()
    寫手.前往(-307,-220)
    寫手.寫('Move "spaceship" to yellow dot using up/left/right-arrow-keys!',
                 font = ("Courier", 12, "bold") )

def turnleft():
    左轉(10)

def turnright():
    右轉(10)

def rueckstoss():
    global vx, vy
    from math import sin, cos, pi
    alpha = 頭向() * pi / 180.0
    vx += FORCE_UNIT * cos(alpha)
    vy += FORCE_UNIT * sin(alpha)

def steps():
    global result
    x,y=位置()
    設位置(x+vx, y+vy)
    if (110 < 距離(target) < 135 and
          8 < 朝向(0,0) < 352):
        result = "CRASH!" 
    elif 距離(target) > 450:
        result = "ESCAPED!"
    elif 距離(target) < 15:
        result = "SUCCESS!"
    if not result:
        在計時後(steps)
    
def go():
    global result
    result = 無
    # Ein Spiel!
    startzeit = clock()
    steps()
    # ouptut result!
    寫手.前往(-305,-200)
    寫手.筆色(紅)
    寫手.寫(result, font=boldfont, move=1)
    if result == "SUCCESS!":
        zeit = clock() - startzeit
        寫手.寫(" (%2.2f s)" % zeit, font=boldfont, move=1)
    寫手.筆色(黑)
    寫手.寫(" New game: spacebar", font=normalfont)

def spiel():
    if result:  # i.e. if game over
        開始()
        go()

def 主函數():
    global designer, 寫手
    designer = 龜類()
    寫手 = 龜類()
    追蹤(1,0)

    global result
    在按鍵時(turnleft,向左鍵)
    在按鍵時(turnright,向右鍵)
    在按鍵時(rueckstoss, 向上鍵)
    在按鍵時(spiel, 空白鍵)
    #onscreenclick(listen)
    聽()
    result = "start"
    scenery()
    在計時後(spiel,500)
    延遲(5)
    # a moment please to ...
    return "EVENTLOOP"

if __name__ == '__main__':
    訊息 = 主函數()
    印(訊息)
    主迴圈()
