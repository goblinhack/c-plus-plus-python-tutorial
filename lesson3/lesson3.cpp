#include <iostream>

//
// A template class describing a 2d Point
//
#include "point.h"

//
// ANSI escape codes
//
#include "ansi.h"

//
// Terminal info
//
#include "terminal.h"

//
// Line drawing
//
#include "line.h"

int main (int argc, char *argv[])
{
    Terminal term;

    term.clear_screen();
    std::cout << term.get_code(term.FOREGROUND_RED);
    Line(&term, Point(4, 4), Point(term.size.x - 4, term.size.y - 4)).draw('r');
    std::cout << term.get_code(term.FOREGROUND_GREEN);
    Line(&term, Point(term.size.x - 4, 4),
         Point(term.size.x - 20, term.size.y - 4)).draw('r');

    std::cout << term.get_bgfg_code(term.BACKGROUND_BLUE,
                                        term.FOREGROUND_WHITE);
    Line(&term, Point(0, 0), Point(0, term.size.y - 2)).draw(' ');
    Line(&term, Point(term.size.x - 1, 0),
         Point(term.size.x - 1, term.size.y - 2)).draw(' ');
    Line(&term, Point(0, 0), Point(term.size.x - 1, 0)).draw(' ');
    Line(&term, Point(0, term.size.y - 2),
         Point(term.size.x - 1, term.size.y - 2)).draw(' ');

    term.set_cursor_bottom_left();
    std::cout << term.get_code(term.RESET);
    std::cout << term.get_code(term.FOREGROUND_GREEN);
    std::cout << "C++: Line draw demo";
    std::cout << term.get_code(term.RESET);
    std::cout << std::endl;

    return (0);
}
