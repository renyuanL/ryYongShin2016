"""       turtle-example-suite:

           tdemo_tangram.py

Inspired by Pavel Boytchev's Elica-Logo
implementation of the tangram game.

"Thanks, I checked the source of the rhomb.
It looks really short. Actually, the whole
tangram.py is much shorter than I have
expected ;)" - Pavel

Use left mouse button to drag, middle
and right mouse button clicks to turn tiles,
left button doubleclick to flip rhomboid.
"""
from turtle_tc import *; from turtle_tc import 龜類, 幕類, 向量類 
from button import Button
import sys, random, time

from tangramdata import tangramdata
sys.setrecursionlimit(20000)
startdata = tangramdata[0]
tangramdata = tangramdata[1:]
A = 198.0
a = A / 4.0
d = a * 2**.5
幕 = 幕類()

def makerhomboidshapes():
    designer.形狀(方形)
    designer.形狀大小(5, 2.5)
    designer.扭曲因子(-1)    # needs Python 3.1
    designer.傾斜(90)
    幕.登記形狀("rhomboid1", designer.取形狀多邊形())
    designer.扭曲因子(1)
    幕.登記形狀("rhomboid2", designer.取形狀多邊形())

class TStein(龜類):
    def __init__(我, 尺寸, 形狀="arrow", clickable=真):
        龜類.__init__(我)
        我.尺寸 = 尺寸
        我.提筆()
        我.形狀(形狀)
        我.重設大小模式("user")
        我.龜大小(尺寸,尺寸,3)
        我.clicktime = -1
        if clickable:
            我.在點擊時(我.turnleft, 2)
            我.在點擊時(我.turnright, 3)
            我.在點擊時(我.store, 1)
            我.在拖曳時(我.移動, 1)
            我.在鬆開時(我.match, 1)
    def turnleft(我,x,y):
        我.左轉(15)
        幕.更新()
    def turnright(我,x,y):
        我.右轉(15)
        幕.更新()
    def store(我,x,y):
        我.clickpos = 向量類(x,y)
    def 移動(我,x,y):
        neu = 向量類(x,y)
        我.前往(我.位置() + (neu-我.clickpos))
        我.clickpos = neu
        幕.更新()
    def place(我, x, y, h):
        我.前往(x,y)
        我.設頭向(h)
    def match(我, x=無, y=無):
        matching = 假
        for cand in STiles:
            if 我.尺寸 == cand.尺寸 and 我.形狀() == cand.形狀():
                if 我.距離(cand) < 20:
                    i = STiles.index(cand)
                    if i < 5 and 我.頭向() == cand.頭向():
                        matching = cand
                    elif (i in [0,1] and
                          STiles[0].距離(STiles[1])<5
                          and (我.頭向()-cand.頭向())%90==0):
                        matching = cand
                    elif (i in [3,4] and
                          STiles[3].距離(STiles[4])<5
                          and (我.頭向()-cand.頭向())%90==0):
                        matching = cand
                    elif i == 5 and (我.頭向()-cand.頭向())%90 == 0:
                        matching = cand
                    elif (i == 6 and 我.flipped == cand.flipped and
                          (我.頭向()-cand.頭向())%180 == 0):
                        matching = cand
                    if matching:
                        我.設位置(cand.位置())
                        break
        幕.更新()


class TRhomboid(TStein):
    def __init__(我, clickable=真):
        TStein.__init__(我, 1, 形狀="rhomboid1", clickable=clickable)
        我.flipped = 假
        我.提筆()
    def flip(我):
        if not 我.flipped:
            我.形狀("rhomboid2")
            我.flipped = 真
        else:
            我.形狀("rhomboid1")
            我.flipped = 假
        幕.更新()
    def store(我, x, y):
        clicktime = time.clock()
        if clicktime - 我.clicktime < 0.4:
            我.flip()
            我.clicktime = -1
        else:
            我.clicktime = clicktime
        我.clickpos = 向量類(x,y)
        
def 起始化():
    global TTiles, STiles, designer
    幕.模式(角度從北開始順時針)
    幕.追蹤(假)
    designer = 龜類(visible=假)
    designer.提筆()
    makerhomboidshapes()
    幕.背景色("gray10")
    STiles = [TStein(A/20., clickable=假),
              TStein(A/20., clickable=假),
              TStein(2*d/20., clickable=假),
              TStein(A/40., clickable=假),
              TStein(A/40., clickable=假),
              TStein(d/20., 方形, clickable=假),
              TRhomboid(clickable=假)]
    TTiles = [TStein(A/20.),
              TStein(A/20.),
              TStein(2*d/20.),
              TStein(A/40.),
              TStein(A/40.),
              TStein(d/20., 方形),
              TRhomboid()]
    for s in STiles:
        s.顏色((1,1,0.9))
        s.龜大小(s.尺寸, s.尺寸, 2)
        s.藏龜()
    幕.更新()
    designer.前往(-390,-288)
    designer.筆色("gray70")
    designer.寫("Inspired by Pavel Boytchev's Elica-Logo implementation of the tangram game",
                   font=("Courier", 10, "bold"))
    nextBtn = Button("next.gif", resetgame)
    nextBtn.設位置(320,220)
    helpBtn = Button("help.gif", helpme)
    helpBtn.設位置(320,-220)

def resetTiles():
    c1, c2, c3 = random.random()/2, random.random()/2, random.random()/2
    arrangeTiles(startdata, TTiles)
    if TTiles[6].flipped:
        TTiles[6].flip()
    if STiles[6].flipped:
        STiles[6].flip()
    for i in 範圍(7):
        TTiles[i].筆色(c1, c2, c3) 
        TTiles[i].填色(c1+random.random()/2, c2+random.random()/2, c3+random.random()/2) 

def arrangeTiles(data, tileset):
    flip = data[-1] == -1
    l = data[:7]
    for i in 範圍(7):
        x,y,h = data[i]
        if i==6 and flip:
            tileset[6].flip()
        tileset[i].place(x, y, h)

def resetgame():
    data = random.choice(tangramdata)
    resetTiles()
    arrangeTiles(data, STiles)
    for t in TTiles+STiles: t.顯龜()
    幕.更新()

def helpme():
    c = STiles[0].筆色()
    x,y,s = STiles[0].龜大小()
    for t in STiles:
        t.筆色(黑)
        t.龜大小(t.尺寸, t.尺寸, 1)
    幕.更新()
    time.sleep(0.5)
    幕.追蹤(假)
    for t in STiles:
        t.筆色(c)
        t.龜大小(t.尺寸, t.尺寸, s)
    幕.更新()

def 主函數():    
    起始化()    
    resetgame()
    return "EVENTLOOP"

if __name__ == "__main__":
    訊息 = 主函數()
    印(訊息)
    幕.主迴圈()
