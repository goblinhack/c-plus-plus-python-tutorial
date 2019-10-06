'''
lesson2 - get the terminal size
'''

from terminal import Terminal
import sys


def lesson2():
    """ term size """
    term = Terminal()

    sys.stdout.write(term.get_code(term.Code.FOREGROUND_GREEN))
    sys.stdout.write("Python: Your terminal size is {}".format(term.size))
    sys.stdout.write(term.get_code(term.Code.RESET))

lesson2()
