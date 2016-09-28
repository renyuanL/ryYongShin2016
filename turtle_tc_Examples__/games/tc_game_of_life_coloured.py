from turtle_tc import *; from turtle_tc import 龜類, 幕類
import time

try:
    import psyco
    from psyco.classes import *
    psyco.full()
    印 ("PSYCO -- SUPER!!")
except:
    印 ("-- psyco not installed - reduced performance --")
    印 ("-- Download psyco at http://psyco.sourceforge.net/ --")

# MAX_X and MAX_Y must be odd
MAX_X = 79
MAX_Y = 57
SQUARE_WIDTH = 10 # must be even
FREEROWS = 3
WINHEIGHT = MAX_Y + FREEROWS
MARG_X = 2 + SQUARE_WIDTH//2   
MARG_Y = 8
DM = 10

幕 = 幕類()

def 座標們(行, 列):
	return ((-MAX_X//2 + 行)*SQUARE_WIDTH + MARG_X,
                ((-MAX_Y+ FREEROWS)//2  + 列 )*SQUARE_WIDTH + MARG_Y)

def cellindices(x, y):
    return ((x-MARG_X + (SQUARE_WIDTH-1)//2)//SQUARE_WIDTH + MAX_X//2 + 1,
            (y-MARG_Y + (SQUARE_WIDTH-1)//2)//SQUARE_WIDTH + (MAX_Y- FREEROWS)//2)

def calccolor(i):
    i = min(20, i)
    return (1.05-i/20., 0., i/20.-0.05)
    
def generate(狀態):
    NBADDR = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))
    while 真:
        yield 狀態
        cd = {}
        for (x,y) in 狀態:
            for dx, dy in NBADDR:
                xx, yy = x+dx, y+dy
                cd[(xx,yy)] = cd.get((xx,yy), 0) + 1
            cd[(x,y)] = cd.get((x,y), 0) + 10
        cells = [c for c in cd if cd[c] in (3,12,13)]
        state1 = {c:1 for c in cells if c not in 狀態}
        for c in cells:
            if c in 狀態:
                state1[c] = 狀態[c]+1
        狀態 = state1


class Patch(龜類):
    def __init__(我, 行, 列):
        龜類.__init__(我, shape=方形, visible=假)
        我.提筆()
        我.前往(座標們(行, 列))
        我.顏色(黑)
        我.形狀大小((SQUARE_WIDTH-2)/20.0)
        
        
class Game(object):

    def __init__(我):
        幕.追蹤(假)
        幕.設立(width=MAX_X*SQUARE_WIDTH + DM,
                     height = (MAX_Y+FREEROWS)*SQUARE_WIDTH + DM,
                     startx = -20,
                     starty = 20)
        幕.幕大小(MAX_X*SQUARE_WIDTH + DM - 50,
                          (MAX_Y+FREEROWS)*SQUARE_WIDTH + DM -50)
        我.designer = 龜類(visible=假)
        starttime = time.clock()
        我.messagero = 龜類(visible=假)
        我.messagero.提筆()
        我.messagero.筆色(藍)
        我.messagero.前往(0, -(MAX_Y+FREEROWS)*SQUARE_WIDTH/2+6)
        我.message("Please wait a moment!")
        我.designer.筆色("gray90")
        w2 = SQUARE_WIDTH // 2
        for c in 範圍(MAX_X+1):
            x1, y1 = 座標們(c,0)
            x2, y2 = 座標們(c, MAX_Y)
            x1, y1, y2 = x1 - w2, y1 - w2, y2 - w2
            我.直線(x1, y1, x1, y2)
        for r in 範圍(MAX_Y+1):
            x1, y1 = 座標們(0, r)
            x2, y2 = 座標們(MAX_X, r)
            x1, y1, x2 = x1 - w2, y1 - w2, x2 - w2
            我.直線(x1, y1, x2, y1)
        幕.更新()
        我.patches = {}
        for r in 範圍(MAX_Y):
            for c in 範圍(MAX_X):
                我.patches[(c, r)] = Patch(c, r)

        我.狀態 = {(41,33):1, (42,33):1, (43,34):1,
                      (42,32):1, (42,34):1}
        for cell in 我.狀態:
            我.patches[cell].顯龜()
        我.newstate = 無

        stoptime = time.clock()
        印(stoptime - starttime)
        幕.更新()
        幕.在按鍵時(我.run, 空白鍵)
        幕.在按鍵時(幕.再見, 脫離鍵)
        幕.在按鍵時(我.清除, "c")
        幕.聽()
        幕.在點擊時(我.toggle)
        我.message("spacebar:start/pause | left click:toggle cell | c:clear"
                     " | escape:quit")

    def message(我, txt):
        我.messagero.清除()
        我.messagero.寫(txt, align="center", font=("Courier", 14, "bold"))
        

    def 直線(我, x1, y1, x2, y2):
        我.designer.提筆()
        我.designer.前往(x1, y1)
        我.designer.下筆()
        我.designer.前往(x2, y2)

    def update_display(我):
        幕.追蹤(假)
        for cell in 我.狀態:
            if cell not in 我.newstate:
                try:
                    我.patches[cell].藏龜()
                except KeyError:
                    pass
        for cell in 我.newstate:
            try:
                我.patches[cell].顯龜()
                我.patches[cell].顏色(calccolor(我.newstate[cell]))
            except KeyError:
                pass
        幕.追蹤(真)

    def 清除(我):
        我.newstate = {}
        我.update_display()
        我.狀態 = {}

    def toggle(我, x, y):
        cell = cellindices(int(x), int(y))
        我.newstate = 我.狀態.copy()
        if cell in 我.newstate:
            del 我.newstate[cell]
        else:
            我.newstate[cell] = 1
        我.update_display()
        我.狀態 = 我.newstate
         

    def run(我):
        starttime = time.clock()
        anzahl_generationen = 0
        幕.在按鍵時(我.停止, 空白鍵)
        generation = generate(我.狀態)
        我.正在跑狀態 = 真
        while 我.正在跑狀態:
            我.newstate = next(generation)
            我.update_display()
            我.狀態 = 我.newstate
            anzahl_generationen +=1
        stoptime = time.clock()
        t = stoptime - starttime
        印(anzahl_generationen, t, anzahl_generationen/t)

    def 停止(我):
        我.正在跑狀態 = 假
        幕.在按鍵時(我.run, 空白鍵)

def 主函數():
    遊戲=Game()
    return "EVENTLOOP"
    

if __name__ == "__main__":
    訊息 = 主函數()
    印(訊息)
    幕.主迴圈()
