'''
本程式檔名：
    moduleTranslate.py= autoTurtle.py

IO：
    turtle.py ----> turtle_tc.py

吃進：
    turtle_tc_alias.py
    turtle_docstringdict_tc.py

2016/07/03

'''


'''
改為輸出turtle_tc檔
本身不再被當作漢化導入執行
2015/12/5
直接執行程式會輸出turtle_c檔
當為import時才不會輸出
2015/11/18
已加上中文說明
2015/11/17
增加輸出一個turtle_c檔
可直接取代turtle_tc運行 
裡面仍需導入turtle模組
但目前還沒加上中文說明
2015/11/16

turtle_tc_2015.py --> turtle_tc.py

Renyuan Lyu
2014/05/25,

last updated: 
2014/12/24, 
2015/01/18

renyuan.lyu@gmail.com
google.com/+RenyuanLyu




Inspired by the MIT Scratch project,
a program language capable of supporting programmers' native language ,
will allow more people ( particularly non-English-speaking kids ) able 
to write the program more fluently.

Starting from Python version 3.0 ,  names of variables, functions, 
and classes  are encoded in utf-8 ,
that is to say, programmers can write programs in their mother languages.
I think this will be a key point to make Python overspread 
even broader and broader.

As long as we can get into many python's modules, provide a set of name aliases 
for each class, method, and import global variables, 
then kids or naive people can also write their own programs. 
Kids include those from K to 12 in non-English-speaking countries, 
who are not fluent nor possess enough vocabulary in English.

This program/module implementing the idea is one of the few first tries,
it is an appendix to the Python built-in modules turtle.py,
which is majorly a bunch of traditional Chinese alias of English name.

This file is named as turtle_tc.py, 
to emphasize it is majorly in traditional Chinese.

Similar modification can be made to make it suitable in any non-English language.

This file can be run by itself,
it can also be put in the path of Python library,
and be imported by the other application of turtle programs

To use Chinese names could not only make the program more readable 
for local Chinese speaking programmers,
it could also make the program more compact, dense and beautiful.

Renyuan Lyu
2014/05/24

renyuan.lyu@gmail.com
google.com/+RenyuanLyu

turtle_tc_01.py

開始超朝向自動翻譯方向前進。

先做出中英對照表。

2014/04/19


============================
用 Python 3，學中文程式設計。
============================

繁體中文龜
----------

使用這個模組，可以讓你使用繁體中文來控制龜畫圖。

作者：呂仁園。
-------------

受了 MIT Scratch project 的啟發，
讓 programming language 能夠以程式員的母語來表達，
將是讓更多人(特別是非英語為母語的小孩)能夠來寫程式的一個關鍵要素。

Python 3.0 以後， 變數、函數、
以及物類、方法、屬性等名稱都使用  Utf-8 編碼，

允許 程式員 運用 其母語來寫作程式，
只要我們鑽進眾多模組內部，為每個物類的函數名稱給個母語別名，
再把相應的 doc 文件說明也轉成母語，
這個基本工程將建立起母語寫作程式的基礎環境，
程式教育就有可能向下紮根，到達高中，甚至是國中的階段。

本程式模組就是在這個想法之下的首次嘗試，
我們把 Python 中， 一個頗負盛名的模組，turtle.py，
為其提供一個繁體中文 (traditional Chinese) 的附加模組，
命名為 turtle_tc.py，

使用者只要把本程式模組放在 python 環境下，模組的搜尋路徑內，
一般為當前程式碼的目錄 (current dir)或是 C:/Python3.x/Lib/，
那麼，你就可以用
import turtle_tc
來取代
import turtle

進而，運用中文來寫基於 龜 的作圖程式，就成為可能。



last updated: 2014/12/24, 2015/01/21

'''
#
# The following are imported in turtle.py originally
# they will not be imported automatically using 
#
# from turtle import *
#
# so we need include them here
#

import tkinter as TK
import types
import math
import time
import inspect
import sys

from os.path import isfile, split, join
from copy import deepcopy
from tkinter import simpledialog

# ############################################


import random

from turtle import *
from turtle import _CFG, _Screen, _Root, TK, _TurtleImage, Tbuffer, TurtleGraphicsError
from turtle import TurtleScreenBase, TurtleScreen, TNavigator, TPen, RawTurtle, Canvas 
#,Terminator, Turtle, Screen,Vec2D,ScrolledCanvas,Shape


#利用inspect可得到模組資訊，主要有四種應用: 類型檢查,獲取源代碼,抓取類和函數信息,解析堆疊
import inspect as ip
#利用random可得到指定範圍的隨機數(沒使用到)
import random as rd

#將龜類的可用的方法詞彙導入
from turtle import __all__
from turtle import getmethparlist 
#, _getpen, _getscreen, _turtle_docrevise, _screen_docrevise #, _Screen, Turtle

'''
隨機數= rd.random
隨機整數= rd.randint
時間= time.time
睡= time.sleep
'''

from turtle_tc_alias import *  ## 把所有別名列表都移出去了

classBeChanged= [
    'Vec2D', 
    'Shape', 
    'TurtleScreenBase', 
    'TurtleScreen', 
    'TNavigator', 
    'TPen', 
    'RawTurtle', 
    '_Screen',  
    'Screen',  # this is a little bit strange, Screen is a function
    'Turtle'
]




def 建立龜模組別名():
    """
    建立龜模組增加中文別名的執行程式碼字串並回傳。
    需要全域變數classBeChanged、turtle模組程式碼及turtle_tc_alias的別名表。
    """
    所有類程式碼=""
    #抓取 classBeChanged 陣列內的 類 名稱
    for 類名稱 in classBeChanged: #= 'TurtleScreenBase'
        #執行字串y變成變數名稱並定義為ey，利用 類 的名稱 抓取烏龜內所有方法
        物類= eval(類名稱)
        #抓取 類 的程式碼
        程式碼= ip.getsource(物類)
        #classTurtleScreenBase=''
        #連接cList字串與 類名稱放入cList
        cList= 'cList'+類名稱
        #利用名稱 抓取類別及方法的中文名稱 串列 (由turtle_tc_alias導入)
        別名表= eval(cList)
        #從第一個開始抓取方法中英名稱，因第零個為類別英中名稱
        for x in 別名表[1:]:
            #抓取方法的中文名稱
            for n in range(1,len(x)):
                # 空四格，為了在 Class類 裡命名方法中文別名，
                # 因此將其組成中文名稱(x[n])等於英文名稱(x[0])字串
                別名指令= ' '*4 + x[n] +'= '  + x[0] +'\n'
                # 物類 內， 有 4 個空白
                # 將命名別名指令加入到抓取的程式碼裡
                程式碼+= 別名指令
        #抓取類中英名稱對照。舉例:('TurtleScreen','龜幕類', '烏龜螢幕類')
        物類別名= 別名表[0] 
        #抓取 Class(類) 中文名稱
        for n in range(1,len(物類別名)):
            # 因其別名命名在 Class(類)外，所以不需 4 個空白，
            # 組成物件類中文名稱(物類別名[n])等於物件類英文名稱(物類別名[0])字串
            類別名指令= 物類別名[n] +'= '  + 物類別名[0] +'\n'
            # 物類 外， 無 4 個空白。
            # 將命名別名加入到程式碼裡
            程式碼+= 類別名指令

        #print(程式碼)
        #執行程式碼，將中文別名加入
        所有類程式碼+= 程式碼
    return 所有類程式碼


def 建立其他別名():
    """
    建立其他函式增加中文別名的執行程式碼字串並回傳。
    需要turtle_tc_alias的別名表。
    """
    #存取命名別名運算式字串
    別名表 = 字串別名表 + 函數別名表
    別名指令碼=''
    #抓取別名表內中英表
    for e in 別名表:
        #exec(e[1] + '=' + e[0] )
        #抓取表內的中文名稱(第零個為英文名稱，所以從第一個開始)
        for n in range(1,len(e)):
            #組成英文名稱(x[0])等於類中文名稱(x[n])字串
            別名指令碼 += e[n] + '=  '+ e[0] + '\n'
    #執行運算式，將中文別名加入
    return 別名指令碼


def 建立中英對照表():
    """
    無傳入參數。但需導入turtle_tc_alias。
    建立一個別名中英對照表並回傳(list型態)。
    包含龜模組別名跟其他別名中英對照表。
    其會根據字母排序。
    """
    別名表單=[]
    #抓取全部別名表(總別名表，宣告在turtle_tc_alias)，為了將全部別名加入到別名表單
    for y in 總別名表:
        #抓取別名表內中英對照名稱
        for x in y:
            #將別名表加到X裡
            別名表單 += [x]
    #將X重新排列產生一個新的排序列表
    中英對照表= sorted(別名表單)
    return 中英對照表


def 印中英對照表(中英對照表):
    """
    印中英對照表(中英對照表)
    
    將中英對照表加上數字印出。
    傳入 中英對照表(list型態表單)，由 建立中英對照表() 所產生。
    """
    #建立表單標題
    print('-'*20)
    print('中英對照表')
    print('-'*20)
    #印出表單，並在表單前加入數字
    for i,x in enumerate(中英對照表):
        print(i,x)



def 中文幫助文件取代(原碼):
    """
    中文幫助文件取代(原碼)
    
    傳入參數 原碼，亦即為增加中文別名的龜模組程式碼字串。
    將原碼中的方法英文說明改成中文說明並回傳。
    (中文說明在turtle_docstringdict_tc檔)
    """
    文件名 = "turtle_docstringdict_tc"
    訊息='中文說明'
    try:
        #將文件導入
        文件檔 = __import__(文件名)
    except:
        #如果導入失敗，則可能文件不存在，並return結束函式
        print('%s.py 不存在， 略過！ turtle_tc 還是可用，只是沒有中文求助功能！'%文件名)
        return 原碼
    龜模組檔 = __import__("turtle")
    #抓取說明文件字典
    幫助字典 = 文件檔.docsdict
    i= 0
    for key in 幫助字典: #範例: key為'Turtle.back'
        try:
            英文幫助文件= eval("龜模組檔."+key+".__doc__")
            #eval(key).__doc__為方法key的說明文字，
            # 抓取文件的中文說明(幫助字典[key])再加上原本的英文說明(原英文幫助文件[key])
            中文幫助文件= '『%04d  '%(i)+ 訊息 + '』\n'+' '*8+ 幫助字典[key] + '\n'+' '*8
            原碼=原碼.replace(英文幫助文件,中文幫助文件+英文幫助文件) 
            i+= 1
        except:
            print('''%s 說明文件輸入有誤，請檢查： %s
            '''% (文件名, key))
    return 原碼


def 印可用的詞彙別名表():
    """將目前可用的變數及方法函式名稱排序印出。
        需要設置__all__隱藏變數。
    """
    print('-'*10)
    print('可用的詞彙別名表 (中英對照表)')
    print('-'*10)
    #將其排序並印出
    print('__all__= ',sorted(__all__))



def 建立龜類方法呼叫(龜類成員):
    """建立龜類方法，把類別內 函數 釋放到 類別外。
    主要是把 物類內函數 的 (self, ...) 變成  (...)。
    幫助匿名龜使用龜類方法。
    """
    執行語句=""
    方法名稱=[]
    #藉由for迴圈一個一個抓取龜類成員
    for 成員 in 龜類成員:
        #取成員名字，其成員內容為('速度', <function TPen.speed at 0x02CF9C00>)格式
        名稱, 物件位置= 成員
        # 暴力 debug
        if 名稱 == 'screens':
            continue
        #去掉為底線開頭的方法
        if ord(名稱[0])>= ord('a'): 
            #放入名稱進  方法名稱
            方法名稱 += [名稱]
            try:
                #抓取龜類方法的參數，回傳兩個參數，第一個為傳入參數名稱(有包含預設值)，第二個為傳入參數名稱
                #舉例:(fun, btn=1, add=None) (fun, btn, add)
                pl1, pl2 = getmethparlist(eval('龜類.' + 名稱))
                #如果回傳為空，此方法無參數傳入
                if pl1 == "":
                    #如果為空則跳過繼續執行
                    continue
                方法宣告 = ("def %(key)s%(pl1)s: return _取筆().%(key)s%(pl2)s" %
                                               {'key':名稱, 'pl1':pl1, 'pl2':pl2})
                執行語句 += 方法宣告 +'\n'+名稱+".__doc__ = 龜類."+名稱+".__doc__"+"\n\n"
                #eval(名稱).__doc__ = eval('龜類.'+名稱).__doc__ # _turtle_docrevise(eval('龜類.'+名稱).__doc__)
            except:
                print('龜類.' + 名稱 +' No put to main')
    return 執行語句,方法名稱


def 建立_幕類方法呼叫(幕類成員):
    """建立幕類方法，把類別內 函數 釋放到 類別外。
    主要是把 物類內函數 的 (self, ...) 變成  (...)。
    幫助匿名幕類使用幕類方法。
    """
    執行語句=""
    方法名稱=[]
    #藉由for迴圈一個一個抓取_幕類成員
    for 成員 in 幕類成員:
        #取成員名字，其成員內容為('追蹤', <function TurtleScreen.tracer at 0x02BAAF18>)格式
        名稱, 物件位置= 成員
        #去掉為底線開頭的方法
        if ord(名稱[0])>= ord('a'): 
            #放入名稱進  方法名稱
            方法名稱 += [名稱]
            try:
                #抓取_幕類方法的參數
                pl1, pl2 = getmethparlist(eval('_幕類.' + 名稱))
                if pl1 == "":
                    continue
                方法宣告 = ("def %(key)s%(pl1)s: return _取幕().%(key)s%(pl2)s" %
                                               {'key':名稱, 'pl1':pl1, 'pl2':pl2})
                執行語句 += 方法宣告 +'\n'+名稱+".__doc__ = _幕類."+名稱+".__doc__"+"\n\n"
                #eval(名稱).__doc__ = eval('_幕類.'+名稱).__doc__# _screen_docrevise(eval('_幕類.'+名稱).__doc__)
            except:
                print('_幕類.' + 名稱 +' No put to main')
    return 執行語句,方法名稱

def _取筆():
    """宣告一個匿名龜類，當其並不存在時。"""

    if 龜類._pen is None:
        龜類._pen= 龜類()

    return 龜類._pen
#設置 _getscreen的中文別名
def _取幕():
    """宣告一個匿名龜幕類，當其並不存在時。"""
    if 龜類._screen is None:
        龜類._screen = _幕類()  ###### 會不會就是這行搞鬼？？ 有無底線之分！

    return 龜類._screen

def 輸出龜模組執行檔(執行碼, 檔案名="turtle_tc.py"):
    """
    輸出龜模組執行檔(執行碼,檔案名="turtle_c.py")
    
    傳入參數:
        執行碼 - 字串，輸出檔案內容
        檔案名 - 字串，輸出檔案名稱(此處預設為turtle_c.py)
    輸出一個檔案，格式為UTF-8。
    """
    f=open(檔案名,"w",encoding='UTF-8')
    
    f.write(執行碼)
    f.close()


導入程式碼 = '''#!/usr/bin/env python3
"""
turtle_tc.py

this file is automatically generated
Renyuan Lyu, Yung-Hsin Kuo, in 2016, Taiwan
"""

import tkinter as TK
import types
import math
import time
import inspect
import sys

from os.path import isfile, split, join
from copy import deepcopy
from tkinter import simpledialog

import random
from turtle import *
from turtle import _CFG, _Screen, _Root, TK, _TurtleImage, Tbuffer, TurtleGraphicsError
from turtle import TurtleScreenBase, TurtleScreen, TNavigator, TPen, RawTurtle, Canvas 
#,Terminator, Turtle, Screen,Vec2D,ScrolledCanvas,Shape

def _取筆():
    """宣告一個匿名龜類，當其並不存在時。"""

    if 龜類._pen is None:
        龜類._pen= 龜類()

    return 龜類._pen
#設置 _getscreen的中文別名
def _取幕():
    """宣告一個匿名龜幕類，當其並不存在時。"""
    if 龜類._screen is None:
        龜類._screen = _幕類()  ###### 會不會就是這行搞鬼？？ 有無底線之分！

    return 龜類._screen
'''

範例程式= """

'''
以下為範例程式，
作為撰寫中文龜作圖程式之參考。
'''

#from turtle_tc import *

def 陰(半徑, 顏色1, 顏色2):
    筆寬(3)
    顏色(黑, 顏色1)
    開始填()
    畫圓(半徑/2., 180)
    畫圓(半徑, 180)
    左轉(180)
    畫圓(-半徑/2., 180)
    結束填()
    左轉(90)
    提筆()
    前進(半徑*0.35)
    右轉(90)
    下筆()
    顏色(顏色1, 顏色2)
    開始填()
    畫圓(半徑*0.15)
    結束填()
    左轉(90)
    提筆()
    後退(半徑*0.35)
    下筆()
    左轉(90)

def 陰陽主函數():
    重設()
    陰(200, 黑, 白)
    陰(200, 白, 黑)
    藏龜()
    return "Done!"


def switchpen():
    if 下筆嗎():
        提筆()
    else:
        下筆()

def demo1():
    '''老turtle.py的演示 - 模塊'''
    重設()
    追蹤(真)
    提筆()
    後退(100)
    下筆()
    # 畫3個方塊;最後填充

    筆寬(3)
    for i in 範圍(3):
        if i == 2:
            開始填()
        for _ in 範圍(4):
            前進(20)
            左轉(90)
        if i == 2:
            顏色("maroon")
            結束填()
        提筆()
        前進(30)
        下筆()
    筆寬(1)
    顏色(黑)
    # 錯

    追蹤(假)
    提筆()
    右轉(90)
    前進(100)
    右轉(90)
    前進(100)
    右轉(180)
    下筆()
    # 一些文本

    寫("startstart", 1)
    寫("start", 1)
    顏色(紅)
    # 楼梯间

    for i in 範圍(5):
        前進(20)
        左轉(90)
        前進(20)
        右轉(90)
    # 充滿樓梯

    追蹤(真)
    開始填()
    for i in 範圍(5):
        前進(20)
        左轉(90)
        前進(20)
        右轉(90)
    結束填()
    # 更多文本


def demo2():
    '''一些新的功能演示。'''
    速度(1)
    顯龜()
    筆粗(3)
    設頭向(朝向(0, 0))
    半徑 = 距離(0, 0)/2.0
    右轉(90)
    for _ in 範圍(18):
        switchpen()
        畫圓(半徑, 10)
    寫("wait a moment...")
    while 回復暫存區的個數():
        回復()
    重設()
    左轉(90)
    色模式(255)
    長度 = 10
    筆色(綠)
    筆粗(3)
    左轉(180)
    for i in 範圍(-2, 16):
        if i > 0:
            開始填()
            填色(255-15*i, 0, 15*i)
        for _ in 範圍(3):
            前進(長度)
            左轉(120)
        結束填()
        長度 += 10
        左轉(15)
        速度((速度()+1)%12)
    # end_fill（）


    左轉(120)
    提筆()
    前進(70)
    右轉(30)
    下筆()
    顏色(紅,黃)
    速度(0)
    開始填()
    for _ in 範圍(4):
        畫圓(50, 90)
        右轉(90)
        前進(30)
        右轉(90)
    結束填()
    左轉(90)
    提筆()
    前進(30)
    下筆()
    形狀(龜形)

    tri = 取龜()
    tri.重設大小模式("auto")
    turtle = 龜類()
    turtle.重設大小模式("auto")
    turtle.形狀(龜形)
    turtle.重設()
    turtle.左轉(90)
    turtle.速度(0)
    turtle.提筆()
    turtle.前往(280, 40)
    turtle.左轉(30)
    turtle.下筆()
    turtle.速度(6)
    turtle.顏色(藍,橙)
    turtle.筆粗(2)
    tri.速度(6)
    設頭向(朝向(turtle))
    count = 1
    while tri.距離(turtle) > 4:
        turtle.前進(3.5)
        turtle.左轉(0.6)
        tri.設頭向(tri.朝向(turtle))
        tri.前進(4)
        if count % 20 == 0:
            turtle.蓋章()
            tri.蓋章()
            switchpen()
        count += 1
    tri.寫("CAUGHT! ", font=("Arial", 16, "bold"), align="right")
    tri.筆色(黑)
    tri.筆色(紅)

    def baba(xdummy, ydummy):
        清除幕()
        再見()

    time.sleep(2)

    while 回復暫存區的個數():
        tri.回復()
        turtle.回復()
    tri.前進(50)
    tri.寫("  Click me!", font = ("Courier", 12, "bold") )
    tri.在點擊時(baba, 1)

if __name__ == '__main__':

    陰陽主函數()

    demo1()

    demo2()

    主迴圈()
    
    #在點擊時離開()
    
"""

if __name__=='autoTurtle' or __name__=='__main__':
    
    龜模組別名=  建立龜模組別名()
    exec(龜模組別名)
    
    其他別名=   建立其他別名()
    exec(其他別名)

    #抓取龜類成員，回傳按名稱排序的 (name, value) 名稱,物件 對元組列表形式返回
    龜類成員= ip.getmembers(龜類)
    
    #抓取_幕類成員
    _幕類成員= ip.getmembers(_幕類)
    
    #存取要放入可用內至的方法名稱
    methodPutToMain=    []
    cmdString= ''
    
    _幕類執行語句,方法名稱=   建立_幕類方法呼叫(_幕類成員)
    exec(_幕類執行語句)
    
    methodPutToMain +=   方法名稱
    
    龜類執行語句,方法名稱=    建立龜類方法呼叫(龜類成員)
    exec(龜類執行語句)
    
    methodPutToMain +=   方法名稱
    __tcAll__= __all__[:]
    __tcAll__ += methodPutToMain

    __tcAll__ += ['龜幕基類', '龜幕類','龜行類','龜筆類','原生龜類', 'TK'] 
    
    #將龜類以外的別名加入表單
    別名表= 字串別名表 + 函數別名表
    for x in 別名表:
        for y in x[1:]:
            __tcAll__ +=  [y]

    中英對照表=  建立中英對照表()
    __tcAll__ += ['中英對照表']

    __all__= __tcAll__[:]
    
    龜模組別名=  中文幫助文件取代(龜模組別名)
    
    執行碼=  ( 導入程式碼 
            + 龜模組別名 
            + 其他別名 
            + _幕類執行語句 
            + 龜類執行語句
            + 範例程式 
            )
       
    輸出龜模組執行檔( 執行碼 )
    
    中英對照表=  建立中英對照表()
    印中英對照表(中英對照表)
    印可用的詞彙別名表()

    
