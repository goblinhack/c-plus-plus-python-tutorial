import os
from point import Point
from ansi import Ansi

class Terminal(Ansi):
    ''' Ansi terminal '''
    def __init__(self):

        ''' Find how big our terminal is '''
        os_size = os.get_terminal_size() 
        self.size = Point(os_size.columns, os_size.lines);
        super().__init__() 
