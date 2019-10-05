'''
lesson1 - print some colorful hellow world message
'''

from enum import IntEnum
import sys

class Ansii:
    '''
    See

    https://stackoverflow.com/questions/4842424/list-of-ansi-color-escape-sequences#4842438

    For a very thorough explanation of these escape codes
    '''
    def __init__(self):
        self.codes = [
            "[0m", # reset
            "[1m", # bold
            "[2m", # faint
            "[3m", # italic
            "[4m", # underline
            "[5m", # slow_blink
            "[6m", # rapid_blink
            "[7m", # reverse_video
            "[8m", # conceal
            "[9m", # crossed_out
            "[10m", # primary_font
            "[11m", # alt_font1
            "[12m", # alt_font2
            "[13m", # alt_font3
            "[14m", # alt_font4
            "[15m", # alt_font5
            "[16m", # alt_font6
            "[17m", # alt_font7
            "[18m", # alt_font8
            "[19m", # alt_font9
            "[20m", # fraktur
            "[21m", # bold_off_or_double_underline
            "[22m", # normal_color
            "[23m", # not_italic
            "[24m", # underline_off
            "[25m", # blink_off
            "[26m", # unused
            "[27m", # inverse_off
            "[28m", # reveal
            "[29m", # not_crossed_out
            "[30m", # foreground_black
            "[31m", # foreground_red
            "[32m", # foreground_green
            "[33m", # foreground_yellow
            "[34m", # foreground_blue
            "[35m", # foreground_magenta
            "[36m", # foreground_cyan
            "[37m", # foreground_white
            "[38m", # foreground_color2
            "[39m", # default_foreground_color
            "[40m", # background_black
            "[41m", # background_red
            "[42m", # background_green
            "[43m", # background_yellow
            "[44m", # background_blue
            "[45m", # background_magenta
            "[46m", # background_cyan
            "[47m", # background_white
            "[48m", # background_color2
            "[49m", # default_background_color
            "[49m", # unused2
            "[51m", # framed
            "[52m", # encircled
            "[53m", # overlined
            "[54m", # not_framed_or_encircled
            "[55m", # not_overlined
            "[56m", # unused3
            "[57m", # unused4
            "[58m", # unused5
            "[59m", # unused6
            "[60m", # underline2
            "[61m", # double_underline
            "[62m", # overline
            "[63m", # double_overline
            "[64m", # stress_marking
            "[65m", # attributes_off
        ]

        self.code_names = [
            "reset",
            "bold",
            "faint",
            "italic",
            "underline",
            "slow_blink",
            "rapid_blink",
            "reverse_video",
            "conceal",
            "crossed_out",
            "primary_font",
            "alt_font1",
            "alt_font2",
            "alt_font3",
            "alt_font4",
            "alt_font5",
            "alt_font6",
            "alt_font7",
            "alt_font8",
            "alt_font9",
            "fraktur",
            "bold_off_or_double_underline",
            "normal_color",
            "not_italic",
            "underline_off",
            "blink_off",
            "unused",
            "inverse_off",
            "reveal",
            "not_crossed_out",
            "foreground_black",
            "foreground_red",
            "foreground_green",
            "foreground_yellow",
            "foreground_blue",
            "foreground_magenta",
            "foreground_cyan",
            "foreground_white",
            "foreground_color2",
            "default_foreground_color",
            "background_black",
            "background_red",
            "background_green",
            "background_yellow",
            "background_blue",
            "background_magenta",
            "background_cyan",
            "background_white",
            "background_color2",
            "default_background_color",
            "unused2",
            "framed",
            "encircled",
            "overlined",
            "not_framed_or_encircled",
            "not_overlined",
            "unused3",
            "unused4",
            "unused5",
            "unused6",
            "underline2",
            "double_underline",
            "overline",
            "double_overline",
            "stress_marking",
            "attributes_off",
        ]

        self.bgfg_codes = [
            "[40;30m", "[40;31m", "[40;32m", "[40;33m",
            "[40;34m", "[40;35m", "[40;36m", "[40;37m",
            "[41;30m", "[41;31m", "[41;32m", "[41;33m",
            "[41;34m", "[41;35m", "[41;36m", "[41;37m",
            "[42;30m", "[42;31m", "[42;32m", "[42;33m",
            "[42;34m", "[42;35m", "[42;36m", "[42;37m",
            "[43;30m", "[43;31m", "[43;32m", "[43;33m",
            "[43;34m", "[43;35m", "[43;36m", "[43;37m",
            "[44;30m", "[44;31m", "[44;32m", "[44;33m",
            "[44;34m", "[44;35m", "[44;36m", "[44;37m",
            "[45;30m", "[45;31m", "[45;32m", "[45;33m",
            "[45;34m", "[45;35m", "[45;36m", "[45;37m",
            "[46;30m", "[46;31m", "[46;32m", "[46;33m",
            "[46;34m", "[46;35m", "[46;36m", "[46;37m",
            "[47;30m", "[47;31m", "[47;32m", "[47;33m",
            "[47;34m", "[47;35m", "[47;36m", "[47;37m",
        ]

    def get_code(self, code):
        """ Get the ansii escape sequence for the given code """
        code = int(code)
        assert code < len(self.codes)
        return self.codes[code]

    def get_code_name(self, code):
        """ Get the human readable name for the ansii escape sequence """
        code = int(code)
        assert code < len(self.codes)
        return self.code_names[code]

    def get_bgfg_code(self, bg_col, fg_col):
        """
        For speed and to avoid converting strings, we have a special lookup
        for background and foreground combinations.
        """
        bg_col -= Ansii.Code.BACKGROUND_BLACK
        fg_col -= Ansii.Code.FOREGROUND_BLACK
        bg_col = int(bg_col)
        fg_col = int(fg_col)
        code = bg_col * 8 + fg_col
        assert code < len(self.codes)
        return self.bgfg_codes[code]

    class Code(IntEnum):
        """ Raw ANSII escape codes """
        RESET = 0
        BOLD = 1
        FAINT = 2
        ITALIC = 3
        UNDERLINE = 4
        SLOW_BLINK = 5
        RAPID_BLINK = 6
        REVERSE_VIDEO = 7
        CONCEAL = 8
        CROSSED_OUT = 9
        PRIMARY_FONT = 10
        ALT_FONT1 = 11
        ALT_FONT2 = 12
        ALT_FONT3 = 13
        ALT_FONT4 = 14
        ALT_FONT5 = 15
        ALT_FONT6 = 16
        ALT_FONT7 = 17
        ALT_FONT8 = 18
        ALT_FONT9 = 19
        FRAKTUR = 20
        BOLD_OFF_OR_DOUBLE_UNDERLINE = 21
        NORMAL_COLOR = 22
        NOT_ITALIC = 23
        UNDERLINE_OFF = 24
        BLINK_OFF = 25
        UNUSED = 25
        INVERSE_OFF = 27
        REVEAL = 28
        NOT_CROSSED_OUT = 29
        FOREGROUND_BLACK = 30
        FOREGROUND_RED = 31
        FOREGROUND_GREEN = 32
        FOREGROUND_YELLOW = 33
        FOREGROUND_BLUE = 34
        FOREGROUND_MAGENTA = 35
        FOREGROUND_CYAN = 36
        FOREGROUND_WHITE = 37
        FOREGROUND_COLOR2 = 38
        DEFAULT_FOREGROUND_COLOR = 39
        BACKGROUND_BLACK = 40
        BACKGROUND_RED = 41
        BACKGROUND_GREEN = 42
        BACKGROUND_YELLOW = 43
        BACKGROUND_BLUE = 44
        BACKGROUND_MAGENTA = 45
        BACKGROUND_CYAN = 46
        BACKGROUND_WHITE = 47
        BACKGROUND_COLOR2 = 48
        DEFAULT_BACKGROUND_COLOR = 49
        UNUSED2 = 49
        FRAMED = 51
        ENCIRCLED = 52
        OVERLINED = 53
        NOT_FRAMED_OR_ENCIRCLED = 54
        NOT_OVERLINED = 55
        UNUSED3 = 56
        UNUSED4 = 57
        UNUSED5 = 58
        UNUSED6 = 59
        UNDERLINE2 = 60
        DOUBLE_UNDERLINE = 61
        OVERLINE = 62
        DOUBLE_OVERLINE = 63
        STRESS_MARKING = 64
        ATTRIBUTES_OFF = 65

def lesson1():
    """ hello beautiful world """
    ansii = Ansii()

    for bg_col in range(ansii.Code.BACKGROUND_BLACK,
                        ansii.Code.BACKGROUND_WHITE):
        for fg_col in range(ansii.Code.FOREGROUND_BLACK,
                            ansii.Code.FOREGROUND_WHITE):
            sys.stdout.write(ansii.get_code(bg_col))
            sys.stdout.write("{0: <20}".format(ansii.get_code_name(bg_col)))
            sys.stdout.write(ansii.get_code(ansii.Code.RESET))
            sys.stdout.write(ansii.get_code(fg_col))
            sys.stdout.write("{0: <20}".format(ansii.get_code_name(fg_col)))
            sys.stdout.write(ansii.get_code(ansii.Code.RESET))
            sys.stdout.write(ansii.get_bgfg_code(bg_col, fg_col))
            sys.stdout.write("combined")
            sys.stdout.write(ansii.get_code(ansii.Code.RESET))
            print()

    sys.stdout.write(ansii.get_code(ansii.Code.FOREGROUND_RED))
    sys.stdout.write("hello")

    sys.stdout.write(ansii.get_code(ansii.Code.FOREGROUND_GREEN))
    sys.stdout.write(" beautiful")

    sys.stdout.write(ansii.get_code(ansii.Code.FOREGROUND_CYAN))
    sys.stdout.write(" colorful")

    sys.stdout.write(ansii.get_code(ansii.Code.FOREGROUND_BLUE))
    sys.stdout.write(" world")

    sys.stdout.write(ansii.get_code(ansii.Code.RESET))
    print(" from Python")

lesson1()
