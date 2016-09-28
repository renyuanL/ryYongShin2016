"""       turtle-example-suite:

           tdemo_scribble.py

Another very rudimentary paint program

- use left mouse button to move turtle
  (by clicking) or to drag it drawing.
- middle mouse button to toggle fill-state
  (watch fillindicator)
- colorbuttons: left button sets pe>>> ================================ RESTART ================================
ncolor,
  right button sets fillcolor
- keys 123456789 set pensize
- spacebar clears drawing
- press backspace to undo recent drawing
  steps.
 -------------------------------------------
                Try to draw!
 -------------------------------------------
          To exit press STOP button
 -------------------------------------------
"""
from turtle_tc import *
import sys
sys.setrecursionlimit(20000)

class ColorButton(龜類):
    def __init__(我, 行, x, y):
        龜類.__init__(我)
        我.提筆(); 我.前往(x, y)
        我.顏色(行)
        我.形狀(方形)
        我.在點擊時(我.setpencolor)
        我.在點擊時(我.setfillcolor, 3)
    def setpencolor(我, x, y):
        筆色(我.筆色())
    def setfillcolor(我, x, y):
        填色(我.筆色())

def 跳(x,y):
    if x > -350:
        提筆(); 前往(x,y); 下筆()

def fill_switch():
    while 真:
        fillindicator.填色(紅)
        yield 開始填()
        fillindicator.填色("")
        yield 結束填()   

def toggle_fill(x, y):
    next(fs)

def 主函數():
    global fs, fillindicator
    設立(800, 600, -20, 20)
    重設()
    形狀("circle")
    形狀大小(0.5)
    速度(0)
    fs = fill_switch() 

    在拖曳時(前往)
    在點擊幕時(跳)
    在點擊幕時(toggle_fill, 2)
    for c in "123456789":
        def setpensize(s=int(c)):
            筆粗(s)
            形狀大小(outline=s)
        在按鍵時(setpensize, c)
    在按鍵時(清除, 空白鍵)
    在按著鍵時(回復, "BackSpace")

    追蹤(假)
    ColorButton(黃, -365, 90)
    ColorButton(橙, -365, 60)
    ColorButton(紅, -365, 30)
    ColorButton("violet", -365, 0)
    ColorButton(藍, -365, -30)
    ColorButton(綠, -365, -60)
    ColorButton(黑, -365, -90)
    fillindicator = 龜類(shape="circle")
    fillindicator.提筆()
    fillindicator.前往(-365, -180)
    fillindicator.顏色(黑, "")
    追蹤(真)
    聽()
    return "DONE!"

if __name__ == "__main__":
    訊息 = 主函數()
    印(訊息)
    主迴圈()
