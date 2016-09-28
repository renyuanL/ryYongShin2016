#!/usr/bin/env python

'''
naturalLangTranslate.py= ryOuterTranslate.py

using GoogleTransalte or similar 
to translate Natural Language,
used in comment or string

'''



#
# old version fails, maybe transfer to newer version
# 2915/04/29
#

#
# https://github.com/soimort/translate-shell
#

# ----------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# <terry.yinzhe@gmail.com> wrote this file. As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return to Terry Yin.
#
# The idea of this is borrowed from <mort.yao@gmail.com>'s brilliant work
#    https://github.com/soimort/google-translate-cli
# He uses "THE BEER-WARE LICENSE". That's why I use it too. So you can buy him a 
# beer too.
# ----------------------------------------------------------------------------
'''
This is a simple, yet powerful command line translator with google translate
behind it. You can also use it as a Python module in your code.
'''
#
# Thanks to https://github.com/terryyin/google-translate-python/blob/master/translate.py
#

import re
import json
from textwrap import wrap
try:
    import urllib2 as request
    from urllib import quote
except:
    from urllib import request
    from urllib.parse import quote

def main():

    translator= Translator(from_lang='en', to_lang= 'zh-TW')#'zh-tw')

    #text= 'Hello, world.'
    
    text= """An example adapted from the example-suite
            of PythonCard's turtle graphics."""

    translation = translator.translate(text)

    print(text, '\n','-'*10,'\n', translation)

class Translator:
    def __init__(self, to_lang, from_lang= 'en'):

        if from_lang == 'auto': from_lang= 'en'
        
        self.from_lang = from_lang
        self.to_lang = to_lang

    def translate(self, source):
        if self.from_lang == self.to_lang:
            return source
        
        #self.source_list = wrap(source, 1000, replace_whitespace=False)
        
        #
        # renyuan: maybe 1000 is too much, make it smaller
        #
        
        #self.source_list = wrap(source, 100, replace_whitespace=False)
        
        self.source_list = source.split('\n')
        # 先照 \n  來切句子。
        # 如此，換行符號才能在以下保留，重新接回來。
        # 但要預防 句子太長，目前尚未預防！
        #
        
        #
        # renyuan: avoid it too long
        # use \n to split it
        #
        '''
        self.source_list = source.split(sep= '\n')
        self.source_list.remove('')
        '''
        X= []
        for s in self.source_list:
            
            if s != '':
                x= self._get_translation_from_online(s)
            else: x= ''
            
            x+= '\n'
            X += [x]
            
        S= ''.join(X)
        S.rstrip('\n') #  刪掉最後一個 \n
        
        return S #''.join(self._get_translation_from_online(s) for s in self.source_list)

    def _get_translation_from_online(self, source):
        json5 = self._get_json5_from_online(source)
        return json.loads(json5)['responseData']['translatedText']

    def _get_json5_from_online(self, source):
        escaped_source = quote(source, '')
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.168 Safari/535.19'}
        req = request.Request(
             url="http://mymemory.translated.net/api/get?q=%s&langpair=%s|%s" % (escaped_source, self.from_lang, self.to_lang)
                 , headers = headers)
        print("http://mymemory.translated.net/api/get?q=%s&langpair=%s|%s" % (escaped_source, self.from_lang, self.to_lang))
             #url="http://translate.google.com/translate_a/t?clien#t=p&ie=UTF-8&oe=UTF-8"
                 #+"&sl=%s&tl=%s&text=%s" % (self.from_lang, self.to_lang, escaped_source)
                 #, headers = headers)
        r = request.urlopen(req)
        return r.read().decode('utf-8')

if __name__ == "__main__":
    
    main()
    #main01()








