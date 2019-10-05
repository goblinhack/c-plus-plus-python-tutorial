'''
lesson3 - get the terminal size
'''

from terminal import Terminal
import sys


def lesson3():
    """ term size """
    term = Terminal()

    sys.stdout.write(term.get_code(term.Code.FOREGROUND_GREEN))
    print("Python: Your terminal size is {}".format(term.size))
    sys.stdout.write(term.get_code(term.Code.RESET))

lesson3()
