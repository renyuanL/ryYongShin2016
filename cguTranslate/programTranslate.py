'''
programTranslate.py=  TurtleTranslate.py

這是本計畫之核心程式，
也是最需改寫的一支程式。

Renyuan Lyu, Yung-Hsin Kuo,
2016/06

'''

'''
1/15
修改了外部翻譯選擇與否

ryTranslate.py

找到了 tokenize.py 這個強大的解析工具，
可以把 .py 解析成 各種類別的 token (塊狀物)。
我們的 python 程式 英翻中，就有譜了。

renyuan, 2015/01/11

又經過一天的奮鬥，

找到了  tn.untokenize(tokenL) 

哈哈哈，就這樣一行搞定！！！

於是，Python 英翻中，就做出來了！！

renyuan, 2015/01/12

藉機 把 turtle_tc 也更新一下 ==> turtle_tc_2015 ==> turtle_tc

也可以做些統計，觀賞一下 頻率分布。

進一步，把那些 普通名稱 (非內定) 也翻譯一下。
更進一步，連 comment, doc_string 也 透過 Google 翻譯一下。
這裡要研究對 Google Translate 下 查詢指令，並撈回答案的技術。

renyuan, 2015/01/13, 

加入更多中英對照表，
但要注意命名空間的衝突。

renyuan, 2015/01/14 

Google Translate 技術成功了！！！
檔頭的說明文件已經可以翻譯。

renyuan, 2015/01/15

把 額外的 80 幾支 程式 都拿來跑跑看，
居然大部分都能跑！

超酷的！
renyuan, 2015/01/15

''' 

#from    ryDic import getDic, getDicE
from    turtle_tc_alias_ext import getDic, getDicE


#import  ryOuterTranslate
import  naturalLangTranslate as ryOuterTranslate

import tokenize as tn
import keyword  as kw
import glob
import os
import sys
import datetime


def 剖析程式碼(檔案):

    # 讀程式檔並把程式印出。
    print(檔案)
    f= open(檔案, 'r', encoding='utf-8')
    程式碼= f.read()
    
    f.seek(0)
   
    
    # 把程式分塊，成為 Token 。
    # 這一行最了不起！！！ 這一波程式急行軍，這一行貢獻最大。
    # 利用generate_tokens 剖析程式碼 => TokenInfo(type=1 (NAME), string='forward', start=(45, 13), end=(45, 20), line='self.forward(24.5 * scale)\n')
    Token= [ x for x in tn.generate_tokens(f.readline) ] 

    f.close()
 
    return 程式碼, Token


def 名稱翻譯(Token表,名字字典, 翻譯字典= None):
    '''
    本函式 很重要，目前暫時達成目的，
    但程式碼不好看，需改寫。 2016/07/01
    '''
    # 讀入要翻譯所根據的字典
    if 翻譯字典==None: 翻譯字典= getDic()
    數量=[0,0,0,0,0]
    括號內= False
    本程式內部函數們= []
    本程式內部類們= ['TurtleScreenBase','TurtleScreen','TNavigator','TPen','RawTurtle','_Screen','Turtle','Screen','Shape','Vec2D','龜幕基類','龜幕類','龜行類','龜筆類','原龜類','_幕類','龜類','幕類','形狀類','向量類']
    本程式內部類宣告= []
    for n,t in enumerate(Token表):

            
        #
        # 檢查 於 函數 括弧內 的 name= ...
        # e.g. def f( name= 0)
        # 函數內引數名稱，暫不動它。
        # 但 def 內 的 函數引數，仍然要翻譯。
        #
        if t.string == '(':
            
            括號內= True

            呼叫的物類名= None
            呼叫的函數名= None
            這行有def嗎= ('def ' in t.line) 
            if 這行有def嗎==True:
                本程式內部函數們 += [Token表[n-1].string]
            else:
                呼叫的函數名= Token表[n-1].string
            這行有class嗎= ('class ' in t.line) 
            if 這行有class嗎==True:
                本程式內部函數們 += [Token表[n-1].string]
            else:
                呼叫的函數名= Token表[n-1].string
            if Token表[n-1].string =="__init__" and Token表[n-2].string ==".":
                呼叫的物類名= Token表[n-3].string

        if 括號內 == True:
            if t.string==')':
                括號內 = False

            是否為括號內部參數= all([ 括號內, 
                                  (t.type==tn.NAME), 
                                  (Token表[n+1].string=='=')]) 
            
            if 是否為括號內部參數==True:  
                if 這行有def嗎==False:
                    if(呼叫的函數名 not in  本程式內部函數們):
                        continue     ##(1)
                    if (呼叫的函數名=='__init__') and (呼叫的物類名 not in 本程式內部函數們):
                        # print("111",呼叫的物類名)
                        continue
            

        if (t.type==1):
            import keyword
            數量[0]+=1
            if t.string in keyword.kwlist:
                數量[1]+=1
            else:
                數量[2]+=1
                if t.string in 翻譯字典:
                    數量[3]+=1
                else:
                    數量[4]+=1
            
        if ((t.type==1) or (t.type==3)) and(t.string in 翻譯字典):

            #Token表[n][1]= D[t.string] ##### need to test
            標記型態= t.type
            標記字串= 翻譯字典[t.string]
            開始位置= t.start # 可能也要改
            結束位置= t.end   # 可能也要改
            整行文字= t.line  # 可能也要改

            Token表[n]= tn.TokenInfo(標記型態,標記字串,開始位置,結束位置,整行文字)
        else:
            import keyword
            import builtins
            if t.type==1 and  t.string not in keyword.kwlist and  t.string not in dir(builtins):
                if  t.string in 名字字典:
                    名字字典[t.string]+=1
                else:
                    if Token表[n-1].string == "import" or Token表[n-1].string == "from" or Token表[n-1].string == "as":
                        continue
                    '''elif Token表[n-1].string == ".":
                        if Token表[n-2].string in 本程式內部類宣告:
                            名字字典[t.string]=1
                            print("111111111111111111"+Token表[n-2].string,Token表[n-1].string,t.string)
                            '''
                    名字字典[t.string]=1
                    #print(t.string+"\t"+tn.tok_name[t.type]+"\t%d"%t.type,file=名字檔)
                

    #print('本程式內定函數們= ', 本程式內定函數們)

    return Token表,名字字典,數量



def 外部連結翻譯(Token表,from_l='auto',to_l='zh-tw'):

    翻譯器= ryOuterTranslate.Translator(from_lang=from_l, to_lang=to_l)

    for n,t in enumerate(Token表):
        連結翻譯= False
        註解類型=0
        if ((t.type==tn.STRING) 
            and (  ('"""' in t.string) 
                or ("'''" in t.string) )):

            三引號= '"""' if ('"""' in t.string) else "'''"
            待翻譯文字= t.string.strip(三引號)
            註解類型=1
            連結翻譯= True

        # 檢測是否為註解，如為#!則不進行
        if (    (t.type==tn.COMMENT) 
            and('#' in t.string)
            and('#!' not in t.string)
            ): 
             # 將字串的#去掉
            待翻譯文字= t.string.strip('#')
            註解類型=2
            連結翻譯= True
        
        if 連結翻譯== True:
            try:
                翻譯後文字= 翻譯器.translate(待翻譯文字)
                翻譯後文字= 翻譯文字修正(翻譯後文字)
            except:
                翻譯後文字= '翻譯失敗，網路可能有問題！保留原文 ... ' + 待翻譯文字  
            if 註解類型==1:
                新字串 = "'''" 
                新字串 += 翻譯後文字 
                新字串 += "'''"
            elif 註解類型==2:
                新字串 = "# " 
                新字串 += 翻譯後文字 
                新字串 += ''
            
            標記型態= t.type
            標記字串= 新字串 #D[t.string]
            開始位置= t.start # 可能也要改
            結束位置= t.end   # 可能也要改
            整行文字= t.line  # 可能也要改
            
            Token表[n]= tn.TokenInfo(標記型態,標記字串,開始位置,結束位置,整行文字)
    return Token表

def 翻譯文字修正(文字):
    
    修正列表= [
        ('龜例如套房','龜作圖範例集'),
        ('例子套房',  '範例集'),
        ('例如套房',  '範例集'),
        ('編程',     '程式設計'),
        ('發電機',   '生成器'),
        ('海龜',     '龜'),
        ('克隆',     '複製'),
        ('播放器',   '玩家'),
        ('合肥鵬遠', 'Kolam'),
        ('用戶',    '使用者'),
        ('龜套房示例','龜作圖範例集')
        ]

    for x in 修正列表:
        文字= 文字.replace(x[0], x[1])
    
    return 文字

def 後處理翻譯(程式碼):
    
    L= [
        ('from turtle import *\n',
         'from turtle_tc import *\n'),

        ('import turtle\n',
         'import turtle_tc as turtle; from turtle_tc import *\n'),

        ('from turtle import',
         'from turtle_tc import *; from turtle_tc import'),

        ('# -*- coding: cp1252 -*-', '# 預設編碼為 utf-8'), # 這行當然是暴力，以後可能凡找到 coding: 就刪吧！
        ('TK.主迴圈()','TK.mainloop()')                     # two_canvases.py 中的特例

        ]
    
    for x in L:
        程式碼= 程式碼.replace(x[0], x[1])

    #
    # 以下這行
    # 特別針對 日文
    #
    # _tc ---> _jp, 
    #
    # using this way is no good, 
    # just a test
    #
    #src= src.replace('_tc', '_jp')
    
    return 程式碼


#
# 這是主要的函式。被外界呼叫的函式。
#

def 翻譯檔案(存放目錄, 待翻譯檔案, 外部翻譯= False, 新檔案名= None):
    if os.path.exists("_varName.py"):
        名字模組= __import__("_varName")
        名字字典=名字模組.變數字典
    else:
        名字字典= {}
    if 存放目錄== "":
        pass
    elif not os.path.exists(存放目錄):
        os.mkdir(存放目錄)
    ## 關鍵處理，把程式分塊，(tokenize)，
    #    
    # 切出所有 變數，函數，物類，方法 及它們的形態(type)。
    #
    程式碼, Token表= 剖析程式碼(待翻譯檔案)

    ## 第一級翻譯， 變數，函數，物類，方法。
    Token表,名字字典,數量= 名稱翻譯(Token表,名字字典)
    if 外部翻譯 :
        ## 第二級翻譯，連結外部將長語句字串翻譯
        Token表= 外部連結翻譯(Token表)

    # 由 Token表 把 程式碼 接回來，文法無誤仍可跑。

    中文化程式碼= tn.untokenize(Token表) # 就這樣一行搞定！
    中文化程式碼= 後處理翻譯(中文化程式碼)  # 後處理，大多是暴力法 字串取代。

    #
    # 把翻譯過的程式存起來，
    if 新檔案名== None:
        新檔案名= 'tc_'+ os.path.basename(待翻譯檔案)
    if 存放目錄!= "":
        新檔案名= 存放目錄 + os.path.sep + 新檔案名
    # print(新檔案名)
    翻譯後檔案= open(新檔案名,'w', encoding= 'utf-8')
    翻譯後檔案.write(中文化程式碼)
    翻譯後檔案.close()
    
    with  open("_varName.py", 'w', encoding='utf-8') as 名字檔:
    
        名字字典表= sorted(名字字典.items(), key= lambda i: i[1],reverse = True)
        print("變數字典= {",file= 名字檔)
        宣告字串=""
        for i in 名字字典表:
            宣告字串+="'%s':%d,\n" %(i[0],i[1])
        宣告字串=宣告字串.rstrip(",\n")
        print(宣告字串+"}",file= 名字檔)
        print(os.path.basename(待翻譯檔案)+"\t",數量)
        
        名字檔.close()
    
    return 程式碼,中文化程式碼,Token表,數量



def 中翻英名稱翻譯(Token表, 翻譯字典= None):
    # 讀入要翻譯所根據的字典
    if 翻譯字典==None: 翻譯字典= getDicE()
    
    括號內= False
    本程式內部函數們= []
    
    本程式內部類們= ['TurtleScreenBase','TurtleScreen','TNavigator','TPen',
        'RawTurtle','_Screen','Turtle','Screen','Shape','Vec2D',
        '龜幕基類','龜幕類','龜行類','龜筆類','原龜類','_幕類',
        '龜類','幕類','形狀類','向量類']
        
    本程式內部類宣告= []
    for n,t in enumerate(Token表):

            
        #
        # 檢查 於 函數 括弧內 的 name= ...
        # e.g. def f( name= 0)
        # 函數內引數名稱，暫不動它。
        # 但 def 內 的 函數引數，仍然要翻譯。
        #
        if t.string == '(':
            
            括號內= True
            呼叫的物類名=''
            呼叫的函數名= None
            這行有def嗎= ('def ' in t.line) 
            #如果這行是函數定義，因現在位置是括號，所以減1便會是函數名字，將其記錄下來。範例: def 函數名():
            if 這行有def嗎==True:
                本程式內部函數們 += [Token表[n-1].string]
            else: #如果不是，則通常為呼叫函數的內部參數設定括號，則減1將其函數記錄下來。範例: print(文字)
                呼叫的函數名= Token表[n-1].string
            這行有class嗎= ('class ' in t.line) 
            if 這行有class嗎==True:
                本程式內部函數們 += [Token表[n-1].string]
                # print(呼叫的物類名)
            else: #如果不是，則通常為呼叫函數的內部參數設定括號，則減1將其函數記錄下來。範例: print(文字)
                呼叫的函數名= Token表[n-1].string
            if Token表[n-1].string =="__init__" and Token表[n-2].string ==".":
                呼叫的物類名= Token表[n-3].string

        if 括號內 == True:
            if t.string==')':
                括號內 = False
            #檢測是否在括號內，是否為NAME型態，是否其下一個為=，如都為是則為是。
            這是函數內引數名稱嗎= all([ 括號內, 
                                  (t.type==tn.NAME), 
                                  (Token表[n+1].string=='=')]) 
            
            #這行有def= ('def ' in t.line) 
            #查看是否呼叫的函數是否為此程式的內部函數，如果不是則為外部設定，所以跳過不處理。
            if 這是函數內引數名稱嗎==True:  
                if 這行有def嗎==False:
                    if(呼叫的函數名 not in  本程式內部函數們):
                        continue     ##(1)
                    if (呼叫的函數名=='__init__') and (呼叫的物類名 not in 本程式內部函數們):
                        # print("111",呼叫的物類名)
                        continue
            #if 這是函數內引數名稱: continue # 這樣比較保守。 ##(2)
            
            #
            # 但 這保守型也會出錯！在同樣函數中！
            # def 測試(l=200, n=4, fun=日, startpos=(0,0), th=2):
            #     函數(l, n)
            #
            # 這個真是兩難！
            #
            # 所以這裡要再細想！！！
            #
            # 先再調回 ##(1)
            #
            
        #
        # 以上仍然碰到難題： 2015/01/19
        #
        # in penrose.py ...
        #
        # def 測試(l=200, n=4, 函數=日, 開始位置=(0,0), th=2):
        #
        # 測試(600, 8, startpos=(70, 117))
        #
        # 這裡要處理的是：
        # 1. 函數內的「帶名字的引數」名稱 (named argument)
        #
        #    若本函數 定義與於本程式內部，
        #    則「定義」與「呼叫」一律照正常情形翻譯
        #
        #    但若函數沒有定義在此，則其「呼叫」之 「帶名字的引數」名稱
        #    應該跳過，不翻譯，保持英文名。
        #
        #  以上描述似乎需要用更進一步的程式邏輯解決，
        #  上面幾行程式碼尚不足以支持這樣的邏輯。
        #   
        #  依上例，如何得知 測試() 這個函數，是在本程式中定義的呢？ 
        #  亦即 def 測試(): 也在本程式 中  
        #
        #   renyuan, 2015/01/19
        #
        #   penrose.py 解決，2015/01/20
        #
        #   這一塊 仍有改善空間。
        #
        #   果然， trigeo.py 又來亂！ 
        #   def __init__() vs 龜類.__init__()
        #
        #   它是 18 支以外，先放著咯！
        #
        
        #
        # 正常的 查字典，
        #
        # 這是最普遍的情形，
        # 但仍需面對 名稱衝突的問題。
        #
        '''if t.string in 本程式內部類們:
            if Token表[n-1].string == '=' and Token表[n+1].string == '(':
                for i in range(n-2,-1,-1):
                    if Token表[i].type==1:break
                本程式內部類宣告+= [Token表[i].string] 
                if Token表[i].string in 翻譯字典:
                    本程式內部類宣告+= [翻譯字典[Token表[i].string]]

                print(本程式內部類宣告)
        if t.string =="class":
            本程式內部類們+= [Token表[n+1].string]
            if Token表[n+1].string in 翻譯字典:
                本程式內部類們+= [翻譯字典[Token表[n+1].string]]
                print(本程式內部類們)'''
        if t.string in 翻譯字典:
            #Token表[n][1]= D[t.string] ##### need to test
            標記型態= t.type
            
            標記字串= 翻譯字典[t.string]
            開始位置= t.start # 可能也要改
            結束位置= t.end   # 可能也要改
            整行文字= t.line  # 可能也要改

            Token表[n]= tn.TokenInfo(標記型態,標記字串,開始位置,結束位置,整行文字)


    #print('本程式內定函數們= ', 本程式內定函數們)

    return Token表



def 中翻英後處理翻譯(程式碼):
    
    L= [
        ('from turtle import *\n',
         'from turtle_tc import *\n'),

        ('import turtle\n',
         'import turtle_tc as turtle; from turtle_tc import *\n'),

        ('from turtle import',
         'from turtle_tc import *; from turtle_tc import'),

        ('# -*- coding: cp1252 -*-', '# 預設編碼為 utf-8'), # 這行當然是暴力，以後可能凡找到 coding: 就刪吧！
        ('TK.主迴圈()','TK.mainloop()')                     # two_canvases.py 中的特例

        ]
    
    for x in L:
        程式碼= 程式碼.replace(x[1], x[0])

    #
    # 以下這行
    # 特別針對 日文
    #
    # _tc ---> _jp, 
    #
    # using this way is no good, 
    # just a test
    #
    #src= src.replace('_tc', '_jp')
    
    return 程式碼


def 中翻英檔案(存放目錄, 待翻譯檔案, 外部翻譯= False, 新檔案名= None ):

    if 存放目錄== "":
        pass
    elif not os.path.exists(存放目錄):
        os.mkdir(存放目錄)
    f= open(待翻譯檔案, 'r', encoding='utf-8')
    程式碼= f.read()
    f.close()
    英文化程式碼= 中翻英後處理翻譯(程式碼)
    f= open('temp12321.py', 'w', encoding='utf-8')
    f.write(英文化程式碼)
    f.close()
    
    ## 關鍵處理，把程式分塊，(tokenize)，
    #    
    # 切出所有 變數，函數，物類，方法 及它們的形態(type)。
    #
    程式碼, Token表= 剖析程式碼('temp12321.py')
    
    os.remove("temp12321.py")
    Token表= 中翻英名稱翻譯(Token表)

    #
    # ryAdded, 2016/07/03, not well tested....
    #
    if 外部翻譯: #True: #外部翻譯 :
        ## 第二級翻譯，連結外部將長語句字串翻譯
        Token表= 外部連結翻譯(Token表, from_l='zh-tw',to_l='en') 
    ##############

    英文化程式碼= tn.untokenize(Token表) # 就這樣一行搞定！
    # 後處理，大多是暴力法 字串取代。

    #
    # 把翻譯過的程式 個別 存起來，
    # print(新檔案名)
    if 新檔案名== None:
        新檔案名= 'te_'+ os.path.basename(待翻譯檔案)
    if 存放目錄!= "":
        新檔案名= 存放目錄 + os.path.sep + 新檔案名
    print(新檔案名)
    翻譯後檔案= open(新檔案名,'w', encoding= 'utf-8')
    翻譯後檔案.write(英文化程式碼)
    翻譯後檔案.close()
    
    return 程式碼,英文化程式碼,Token表

#-----------------------------------------------------------------

if __name__ == '__main__':
    

    存放目錄= ''
    
    檔案in=    '_yinyang.py'
    if os.path.exists(檔案in):
        檔案out=   '_yinyang_tc.py'    
        程式碼, 中文化程式碼, 標記表, 數量= 翻譯檔案(  存放目錄, 待翻譯檔案= 檔案in, 新檔案名= 檔案out, 外部翻譯= True)
        
        檔案in=    '_yinyang_tc.py'
        檔案out=   '_yinyang_en.py'
        程式碼, 英文化程式碼, 標記表=       中翻英檔案(存放目錄, 待翻譯檔案= 檔案in, 新檔案名= 檔案out, 外部翻譯= True)
    
 
    
    
    
    