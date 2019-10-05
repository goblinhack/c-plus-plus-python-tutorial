#include <iostream>

//
// A template class describing a 2d point
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

int main (int argc, char *argv[])
{
    Terminal term;

    std::cout << term.get_code(term.FOREGROUND_GREEN);
    std::cout << "C++: Your terminal size is " << term.size;
    std::cout << term.get_code(term.RESET);

    return (0);
}
