# Button
# 8. 3. 2007
# Gregor Lingl

from turtle_tc import *; from turtle_tc import 龜類

class Button(龜類):
    def __init__(self, picfile, action):
        龜類.__init__(self)
        self.getscreen().register_shape(picfile)
        self.shape(picfile)
        def _action(x,y):
            action()
        self.onclick(_action)
        self.pu()
        self.speed(0)
