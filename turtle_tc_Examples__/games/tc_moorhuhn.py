# 預設編碼為 utf-8
# Autor: Gregor Lingl
# Datum: 17. 9. 2006
# moorhuhn - Spiel

from turtle_tc import *; from turtle_tc import 幕類, 龜類 # title, mainloop
import random, time
try:
    import winsound
    _SOUND = 真
except:
    _SOUND = 假
    印("NO SOUND!")

SHOTS = 10
VELOCITY = 1
WINWIDTH, WINHEIGHT = 800, 600
HIT = "getroffen.wav"
MISSED = "daneben.wav"
GOOD = "gameover.wav"
MODERATE = "applaus.wav"

class MHManager(龜類):
    """Special Turtle, perform the task to manage the Moorhuhn-GUI.
    """
    def __init__(我, w, h):
        龜類.__init__(我, visible=假)
        我.幕 = 幕類()
        我.幕.設立(w, h)
        我.速度(0)
        我.提筆()
        我.前往(-WINWIDTH//2 + 50, -WINHEIGHT//2 + 20)
        我.筆色(黃)
    def message(我, txt):
        """Output text to graphics window.
        """
        我.清除()
        我.寫(txt, font=("Courier", 18, "bold"))

class Huhn(龜類):
    def __init__(我, bilddatei, 遊戲):
        龜類.__init__(我, bilddatei)
        我.遊戲 = 遊戲
        我.提筆()
        我.速度(0)
        我.在點擊時(我.hit)
        我.開始()
    def 開始(我):
        我.藏龜()
        我.設位置(-WINWIDTH//2-20, random.randint(-WINHEIGHT//3,WINHEIGHT//3))
        我.vx = random.randint(6,11) * VELOCITY
        我.vy = random.randint(-3,3) * VELOCITY
        我.getroffen = 假
        我.tot = 假
        我.顯龜()
        我.ausdemspiel = 假
    def hit(我, x, y):
        if 我.tot or 我.遊戲.shots==SHOTS: # game over
            return
        我.getroffen = 真
        我.tot = 真
        我.遊戲.score += 1

    def 步進(我):
        if 我.ausdemspiel:
            time.sleep(0.01)  # 
            return
        if 我.tot:
            我.vy = 我.vy - 0.25 * VELOCITY
        x, y = 我.位置()
        x = x + 我.vx
        y = y + 我.vy
        我.前往(x,y)
        if x > WINWIDTH//2 + 20 or abs(y) > WINHEIGHT//2 + 10: 
            if 我.遊戲.shots != SHOTS:
                我.開始()
            else:
                我.ausdemspiel = 真

class MoorhuhnGame(object):
    """Combine elements of Moorhuhn game.
    """
    def __init__(我):
        我.mhm = mhm= MHManager(800, 600) # erzeugt
                                     # Grafik-Fenster
        mhm.幕.背景圖("landschaft800x600.gif")
        mhm.message("Press spacebar to start game!")

        mhm.幕.登記形狀("huhn01.gif")
        mhm.幕.登記形狀("huhn02.gif")
        我.huehner = [Huhn("huhn01.gif", 我), Huhn("huhn02.gif", 我)]
        
        我.gameover = 真   # now a new game can start
        mhm.幕.在點擊時(我.shot, 1)
        mhm.幕.在按鍵時(我.遊戲, 空白鍵)
        mhm.幕.聽()
        mhm.幕.取畫布().config(cursor="X_cursor") # get into Tkinter ;-)
    def 遊戲(我):
        if not 我.gameover:
            return   # altes Spiel l酳ft noch
        我.mhm.message("GAME RUNNING")
        我.shots = 0
        我.score = 0
        我.gameover = 假
        for huhn in 我.huehner:
            huhn.開始()
        while not 我.gameover:
            for huhn in 我.huehner:
                huhn.步進()
            gameover = 我.shots == SHOTS
            for huhn in 我.huehner:
                gameover = (gameover and huhn.ausdemspiel)
            我.gameover = gameover
            
        trefferrate = 1.0*我.score/我.shots
        我.mhm.message( ("Score: %1.2f" % trefferrate) +
                                        " - press spacebar!")
        if trefferrate > 0.55:
            我.sound(GOOD)
        else:
            我.sound(MODERATE)
    def shot(我, x, y):
        if 我.shots == SHOTS:
            return # Es l酳ft kein Spiel, also kein Schuss
        我.shots = 我.shots + 1
        klangdatei = MISSED
        for huhn in 我.huehner:
            if huhn.getroffen: 
                klangdatei = HIT
                huhn.getroffen = 假
                break
        if 我.shots == SHOTS:
            我.mhm.message("GAME OVER!")
        else:        
            我.mhm.message("hits/shots: %d/%d" %(我.score, 我.shots))
        我.sound(klangdatei)
    def sound(我, soundfile):
        if not _SOUND: return
        winsound.PlaySound(soundfile, winsound.SND_ASYNC) 

def 主函數():  # for xturtleDemo
    MoorhuhnGame()
    return "EVENTLOOP"
    
if __name__ == "__main__":
    訊息 = 主函數()
    印(訊息)
    幕類().主迴圈()
