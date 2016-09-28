# Button
# 8. 3. 2007
# Gregor Lingl

from turtle_tc import *; from turtle_tc import 龜類

class Button(龜類):
    def __init__(我, picfile, action):
        龜類.__init__(我)
        我.取幕().登記形狀(picfile)
        我.形狀(picfile)
        def _action(x,y):
            action()
        我.在點擊時(_action)
        我.提筆()
        我.速度(0)
