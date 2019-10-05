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

    term.cls();
    std::cout << term.get_code(term.FOREGROUND_RED);
    Line l(&term, Point(3, 10), Point(20,31));
    l.draw('x');

    term.bottom_left();
    std::cout << term.get_code(term.FOREGROUND_GREEN);
    std::cout << "C++: Line draw demo";
    std::cout << term.get_code(term.RESET);
    std::cout << std::endl;

    return (0);
}
