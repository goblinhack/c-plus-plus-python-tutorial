'''
lesson3 - get the terminal size
'''

from terminal import Terminal
from line import Line
from point import Point
import sys
import point


def lesson3():
    """ term size """
    term = Terminal()

    term.clear_screen();
    sys.stdout.write(term.get_code(term.Code.FOREGROUND_RED))
    l = Line(term, Point(3, 10), Point(20,31))
    l.draw('x');

    term.set_cursor_bottom_left()
    sys.stdout.write(term.get_code(term.Code.FOREGROUND_GREEN))
    print("Python: Line draw demo")
    sys.stdout.write(term.get_code(term.Code.RESET))

lesson3()
