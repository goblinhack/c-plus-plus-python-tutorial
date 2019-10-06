import os
import sys
from point import Point
from ansi import Ansi

class Terminal(Ansi):
    ''' Ansi terminal '''
    def __init__(self):

        ''' Find how big our terminal is '''
        os_size = os.get_terminal_size() 
        self.size = Point(os_size.columns, os_size.lines)

        ''' Save the jump codes for moving the cursor '''
        self.save_cursor_codes()
        super().__init__() 

    def set_cursor(self, p):
        assert (p.x >= 0) and (p.x < self.size.x)
        assert (p.y >= 0) and (p.y < self.size.y)
        sys.stdout.write(self.cursor_codes[p.x][p.y])

    def clear_screen(self):
        self.set_cursor(Point(0, 0))
        sys.stdout.write("\033[2J")

    def set_cursor_bottom_left(self):
        self.set_cursor(Point(0, self.size.y-1))

    def set_cursor_bottom_right(self):
        self.set_cursor(Point(self.size.x-1, self.size.y-1))

    def set_cursor_top_left(self):
        self.set_cursor(Point(0, 0))

    def set_cursor_top_right(self):
        self.set_cursor(Point(self.size.x-1, 0))

    def save_cursor_codes(self):
        '''
        You can write this loop in two ways. This way is faster
        '''
        self.cursor_codes = [["\033[{};{}H".format(y, x) \
                                for y in range(self.size.y)] \
                                   for x in range(self.size.x)]
        '''
        But this is more readable
        self.cursor_codes = []
        for x in range(0, self.size.x):
            self.cursor_codes.append([])
            for y in range(0, self.size.y):
                self.cursor_codes[x].append("\033[{};{}H".format(y, x))
        '''
