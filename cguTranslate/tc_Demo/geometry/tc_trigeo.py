"""       turtle-example-suite:

           tdemo_trigeo.py

Implementation of a find of Kirby Urner:

See: pdf_animation_by_ron_resch.pdf at
http://www.4dsolutions.net/presentations/

This version differs slightly from the
original in that the central three triangles
are the upmost, so *they* remain visible
during the animation.
"""

from turtle_tc import *; from turtle_tc import 龜類, 幕類, 向量類
import math

def dsin(角度):
    return math.sin(角度*math.pi/180)

class TriTurtle(龜類):
    def __init__(我, c, r, tritype):
        龜類.__init__(我, shape="triangle")
        我.c = c
        我.r = r
        我.速度(0)
        我.筆色(0,0,0)
        if tritype == 1:
            我.basecolor = (1.0, 0.80392, 0.0)
            我.f = -1
            我.左轉(30)
        else:
            我.basecolor = (0.43137, 0.43137, 1.0)
            我.f = 1
            我.左轉(90)
        我.填色(我.basecolor)
        我.提筆()
        我.前往(c*A, r*A*3**.5/3)
        我.形狀大小(SHS, SHS, 1)
        我.D = 我.距離(0,0)
        我.e = (1/我.D)*我.位置()
    def setturn(我, φ):
        我.前往(SF*我.D*dsin(90-φ)*我.e)
        我.設傾角(φ*我.f)
        我.形狀大小(SHS*SF)
        if abs(我.c) + abs(我.r) > 2:
            我.填色([x + (1-x)*φ/360 for x in 我.basecolor])
            bc = φ/360.
            我.筆色(bc, bc, bc)
            

def 主函數():
    global d, SHS, SF, A
    A = 42 # answer to the ultimate question ... (you know)
    SHS = A / 20.
    SF = 1.0
    DSF = 1.0038582416
    s = 幕類()
    s.設立(800, 600)
    s.重設()
    s.追蹤(0)
    d = 龜類(visible=假)
    for i in 範圍(6):
        d.前進(500)
        d.後退(500)
        d.左轉(60)   

    triangles = []
    for c in 範圍(-5,6,2):
        if abs(c) != 1:
            triangles.append(TriTurtle(c, 1, 1))
            triangles.append(TriTurtle(c, -1, 2))
    for c in 範圍(-4,5,2):
        if c != 0:
            triangles.append(TriTurtle(c, 2, 2))
            triangles.append(TriTurtle(c, -2, 1))
        triangles.append(TriTurtle(c, -4, 2))
        triangles.append(TriTurtle(c, 4, 1))
    for c in 範圍(-3,4,2):
        triangles.append(TriTurtle(c, 5, 2))
        triangles.append(TriTurtle(c, -5, 1))
        triangles.append(TriTurtle(c, -7, 2))
        triangles.append(TriTurtle(c, 7, 1))
    for c in 範圍(-2,3,2):
        triangles.append(TriTurtle(c, 8, 2))
        triangles.append(TriTurtle(c, -8, 1))
    for c in (-1, 1):
        triangles.append(TriTurtle(c, 1, 1))
        triangles.append(TriTurtle(c, -1, 2))
    triangles.append(TriTurtle(0, 2, 2))
    triangles.append(TriTurtle(0, -2, 1))
    s.追蹤(1)
                         
    for φ in 範圍(1,361):
        SF = SF*DSF
        s.追蹤(0)
        for t in triangles:
            t.setturn(φ)
        s.追蹤(1)
    return "DONE!"

if __name__ == "__main__":
    訊息 = 主函數()
    印(訊息)
    幕類().主迴圈()
