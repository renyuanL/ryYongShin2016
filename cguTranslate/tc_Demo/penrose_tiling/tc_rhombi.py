#!/usr/bin/python
"""       turtle-example-suite:

            tdemo_rhombi.py

Constructs an aperiodic penrose-tiling,
consisting of two types of rhombi, thin and
fat ones, by the method of inflation in six steps.

For more information see:
 http://en.wikipedia.org/wiki/Penrose_tiling
"""

from turtle_tc import *
from time import clock, sleep

f = (5**0.5-1)/2.0   # (sqrt(5)-1)/2 -- goldener Schnitt

def fat(l):
    左轉(36)
    前進(l)
    右轉(72)
    前進(l)
    右轉(108)
    前進(l)
    右轉(72)
    前進(l)
    右轉(144)
    
def skinny(l):    
    左轉(72)
    前進(l)
    右轉(144)
    前進(l)
    右轉(36)
    前進(l)
    右轉(144)
    前進(l)
    右轉(108)

def inflatefat(l, n):
    if n == 0:
        px, py = 位置()
        h, x, y = int(頭向()), round(px,3), round(py,3)
        瓦片字典[(h,x,y)] = 真
        return
    fl = f * l
    左轉(216)
    後退(l)
    inflatefat(fl, n-1)
    左轉(108)
    inflateskinny(fl, n-1)
    前進(l)
    右轉(144)
    inflatefat(fl, n-1)
    左轉(216)
    後退(l)
    inflateskinny(fl, n-1)
    左轉(108)
    inflatefat(fl, n-1)
    前進(l)
    右轉(144)

def inflateskinny(l, n):
    if n == 0:
        px, py = 位置()
        h, x, y = int(頭向()), round(px,3), round(py,3)
        瓦片字典[(h,x,y)] = 假
        return
    fl = f * l
    左轉(252)
    後退(l)
    inflatefat(fl, n-1)
    左轉(216)
    後退(l)
    inflateskinny(fl, n-1)
    左轉(144)
    inflateskinny(fl, n-1)
    前進(l)
    右轉(144)
    inflatefat(fl, n-1)
    前進(l)
    右轉(108)

def 畫(l, n, th=2):
    清除()
    l = l * f**n
    龜大小(l/100.0, l/100.0, th)    
    for k in 瓦片字典:
        h, x, y = k
        設位置(x, y)
        設頭向(h)
        if 瓦片字典[k]:
            形狀("fat")
            顏色(黑, 綠)
        else:
            形狀("skinny")
            顏色(黑, 紅)
        蓋章()

def 製造形狀們():
    追蹤(0)
    開始多邊形()
    fat(100)
    結束多邊形()
    加形狀("fat", 取多邊形())
    開始多邊形()
    skinny(100)
    結束多邊形()
    加形狀("skinny", 取多邊形())
    追蹤(1)

def rsun(l, n):
    for i in 範圍(5):
        inflatefat(l, n)
        左轉(72)

def 開始():
    #winsize(800, 800)
    重設()
    藏龜()
    提筆()
    製造形狀們()
    重設大小模式("user")
    
def 測試(l=300, n=4, 函數=rsun, 開始位置=(0,0), th=2):
    global 瓦片字典
    前往(開始位置)
    設頭向(0)
    瓦片字典 = {}
    a = clock()
    追蹤(0)
    函數(l, n)
    b = clock()
    畫(l, n, th)
    追蹤(1)
    c = clock()
    印("Rechnen:   %7.4f s" % (b - a))
    印("Zeichnen:  %7.4f s" % (c - b))
    印("Insgesamt: %7.4f s" % (c - a))
    nk = len([x for x in 瓦片字典 if 瓦片字典[x]])
    nd = len([x for x in 瓦片字典 if not 瓦片字典[x]])
    印("%d dicke und %d schmale Rhomben = zusammen %d Teile." % (nk, nd, nk+nd))

def 展示(函數=rsun):
    開始()
    for i in 範圍(7):
        測試(200, i, 函數)
        if i < 5:
            sleep(2-i*0.2)

def 主函數():
    #title("Demo: Penrose-Parkettierung mit Rhomben.")
    模式(角度從北開始順時針)
    展示()
    筆色(黑)
    前往(0,-370)
    寫("Please wait for some 15 seconds ...",
          align="center", font=('Courier', 24, 'bold'))
    測試(450, 6)
    return "Done!"

if __name__ == "__main__":
    訊息 = 主函數()
    印(訊息)
    主迴圈()
