#!/usr/bin/env python3
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
    Line(term, Point(4, 4), Point(term.size.x - 4, term.size.y - 4)).draw('r')
    sys.stdout.write(term.get_code(term.Code.FOREGROUND_GREEN))
    Line(term, Point(term.size.x - 4, 4),\
         Point(term.size.x - 20, term.size.y - 4)).draw('r')

    sys.stdout.write(term.get_bgfg_code(term.Code.BACKGROUND_BLUE,
                                        term.Code.FOREGROUND_WHITE))
    Line(term, Point(0, 0), Point(0, term.size.y - 2)).draw(' ')
    Line(term, Point(term.size.x - 1, 0), \
         Point(term.size.x - 1, term.size.y - 2)).draw(' ')
    Line(term, Point(0, 0), Point(term.size.x - 1, 0)).draw(' ')
    Line(term, Point(0, term.size.y - 2), \
         Point(term.size.x - 1, term.size.y - 2)).draw(' ')

    term.set_cursor_bottom_left()
    sys.stdout.write(term.get_code(term.Code.RESET))
    sys.stdout.write(term.get_code(term.Code.FOREGROUND_GREEN))
    print("Python: Line draw demo")
    sys.stdout.write(term.get_code(term.Code.RESET))

lesson3()
