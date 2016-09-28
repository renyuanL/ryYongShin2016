"""       turtle-example-suite:

        tdemo_penrose_animation.py

      contributed by Wolfgang Urban



For more information see:
 http://en.wikipedia.org/wiki/Penrose_tiling
"""

from turtle_tc import *
import math
import time

SPEED = 4

PHI = (1.0+5.0**0.5)/2.0
W = math.pi/180.0

###############################
# create kite and dart turtles
###############################

class MyPen(筆類):
    def __init__(我,尺寸,homepos):
        筆類.__init__(我)
        我.速度(SPEED)
        我.homepos = homepos
        我.顯龜()
        我.提筆()
        我.s = 尺寸
        我.重設大小模式("auto")
        我.筆寬(3)
        我.龜大小(1,1,3)
        我.rest()

    # forward scaled
    def walk(我,d): 我.前進(我.s*d)

    # go to resting position
    def rest(我): 我.設位置(我.homepos)

    # enter the game, home()
    def act(我): 我.設位置(0,0)

    # walk a path
    def travel(我,path):
        for (length,角度) in path:
            我.walk(length)
            我.右轉(角度)
        我.lastpath = path

    # travel backwards
    def backhome(我):
        我.lastpath.reverse()
        for (length,角度) in 我.lastpath:
            我.左轉(角度)
            我.walk(-length)
        我.lastpath = []

    # stamp n adjacent copies, symmetric
    def multistamp(我,n):
        我.左轉((n-1)*72/2)
        for i in 範圍(n-1):
            我.蓋章()
            我.右轉(72)
        我.蓋章()
        我.左轉((n-1)*72/2)
        
##############
# our turtles
##############

class Kite(MyPen):
    def __init__(我,s,myshape):
        MyPen.__init__(我,s,(250,-260))
        我.形狀(myshape)
                              
class Dart(MyPen):
    def __init__(我,s,myshape):
        MyPen.__init__(我,s,(-250,-260))
        我.形狀(myshape)


########################
# paint the Penrose sun    
########################

def 日(s, 風箏, 飛鏢):

    # draw    
    k = Kite(s,風箏)
    d = Dart(s,飛鏢)
    d.速度(2)
    
    k.act()
    for i in 範圍(5):
        k.蓋章()
        k.右轉(72)
    k.rest()

    d.act()
    for i in 範圍(5):
        d.travel([(-1-PHI,0)])
        d.蓋章()
        d.backhome()
        d.右轉(72)
    d.rest()

    k.act()
    for i in 範圍(5):
        k.travel([(PHI,0)])
        k.multistamp(2)
        k.backhome()
        k.右轉(72)

    k.右轉(36)
    for i in 範圍(5):
        k.travel([(2*PHI+1,0)])
        for j in 範圍(5):
            k.蓋章()
            k.右轉(72)
        k.backhome()
        k.右轉(72)
    k.左轉(36)
    k.rest()

    d.act()
    d.左轉(36)
    for i in 範圍(5):
        d.travel([(-2*PHI-1,0)])
        d.multistamp(3)
        d.蓋章()
        d.backhome()
        d.右轉(72)
    d.右轉(36)
    d.rest()

    k.act()
    for i in 範圍(5):
        k.travel([(2*PHI+1,-72),(PHI,36+72)])
        k.multistamp(2)
        k.travel([(0,72), (PHI,-36), (PHI,-72-36)])
        k.multistamp(2)
        k.travel([(0,72+36), (-PHI,-72), (-2*PHI-1,72)])
    k.rest()

    
    d.act()
    for i in 範圍(5):
        d.travel([(-2*PHI-1,-36),(-PHI-1,0)])
        d.蓋章()
        d.travel([(PHI+1,72), (-PHI-1,0)])
        d.蓋章()
        d.travel([(PHI+1,-36), (2*PHI+1,72)])
                 
    d.左轉(36)
    for i in 範圍(5):
        d.travel([(-3*PHI-2,0)])
        d.multistamp(2)
        d.backhome()
        d.右轉(72)
    d.右轉(36)        
    d.rest()

    k.藏龜()
    d.藏龜()


#############################
# build kite and dart shapes
#############################

# shape with color arcs as "kite", "dart"
# ... could be cleaned up a little....
def buildshapes1(s):
    速度(10)
    模式(角度從北開始順時針)
    s = s/PHI
    形狀(龜形)

    # prepare kite shape
    提筆()
    筆寬(3)
    後退(60)
    顏色(黑)
    寫("the Penrose kite",font=("Arial",24),align="center")
    前進(60)

    myshape = 形狀類("compound")
    # black border
    開始多邊形()
    下筆()
    顏色("grey")
    左轉(36)
    前進(s*(PHI+1))
    右轉(108)
    前進(s*PHI)
    右轉(36)
    前進(s*PHI)
    右轉(108)
    前進(s*(PHI+1))
    右轉(144)
    結束多邊形()
    m1 = 取多邊形()
    myshape.加成員(m1,(1.0,0.9,0.9),"grey")
    # blue arc
    顏色(藍)
    提筆()
    左轉(36); 前進(s*PHI); 右轉(90);
    開始多邊形()
    下筆(); 畫圓(-s*PHI,72,10); 提筆()
    右轉(180); 畫圓(s*PHI,72,10);   # connect to starting point
    結束多邊形()
    右轉(90); 後退(s*PHI); 右轉(36)
    m3 = 取多邊形()
    myshape.加成員(m3,白,藍)
    # red arc
    顏色(紅)
    提筆()
    前進(s+s*PHI); 右轉(180-72); 前進(s); 右轉(90)
    開始多邊形()
    下筆();
    畫圓(-s,72*2,10);
    右轉(180);
    畫圓(s,72*2,10);
    提筆()
    結束多邊形()
    左轉(90); 前進(s); 右轉(72)
    後退(s+s*PHI)
    m2 = 取多邊形()
    myshape.加成員(m2,白,紅)
    # build    
    登記形狀("風箏",myshape)
    清除()

    # prepare dart shape
    提筆()
    後退(60)
    顏色(黑)
    寫("the Penrose dart",font=("Arial",24),align="center")
    前進(60)

    筆寬(3)
    myshape = 形狀類("compound")
    # black border
    開始多邊形()
    顏色("grey")
    下筆()
    左轉(36)
    前進(s*(PHI+1))
    右轉(144)
    前進(s*(1+1/PHI))
    左轉(36)
    前進(s*(1+1/PHI))
    右轉(144)
    前進(s*(PHI+1))
    右轉(144)
    結束多邊形()
    m1 = 取多邊形()
    myshape.加成員(m1,(0.9,0.9,1),"grey")
    # blue arc
    顏色(藍)
    提筆()
    左轉(36); 前進(s); 右轉(90);
    開始多邊形()
    下筆(); 畫圓(-s,72,10); 提筆()
    右轉(180); 畫圓(s,72,10);   # connect to starting point
    結束多邊形()
    右轉(90); 後退(s); 右轉(36)
    m3 = 取多邊形()
    myshape.加成員(m3,白,藍)
    # red arc
    顏色(紅)
    提筆()
    前進(s+s/PHI); 右轉(72); 前進(s/PHI); 右轉(90)
    開始多邊形()
    下筆();
    畫圓(-s/PHI,216,10);
    右轉(180);
    畫圓(s/PHI,216,10);
    提筆()
    結束多邊形()
    左轉(90); 前進(s/PHI); 右轉(108)
    後退(s+s/PHI)
    m2 = 取多邊形()
    myshape.加成員(m2,白,紅)
    # build    
    登記形狀("飛鏢",myshape)
    藏龜()
    提筆()

#######################################################################
# demo
#######################################################################

def 主函數():
    s=40
    重設()
    模式(角度從北開始順時針)

    buildshapes1(s)
    清除()
    日(40,"風箏","飛鏢")
    return "Done!"
    
if __name__ == "__main__":
    res = 主函數()
    印(res)
    主迴圈()
