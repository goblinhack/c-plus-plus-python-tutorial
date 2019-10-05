#ifndef TERMINAL_H
#define TERMINAL_H
//
// Terminal routines, like get the size
//
#include <iostream>

#ifndef _WIN32
#include <sys/ioctl.h>
#include <termios.h>
#include <unistd.h> // for STDOUT_FILENO
#endif

//
// A template class describing a 2d point
//
#include "point.h"

//
// Note public is very important here, else you cannot get to public
// members in Ansi
//
class Terminal : public Ansi {
public:
    Terminal() {
        //
        // Find how big our terminal is
        //
        save_terminal_size();
    }

    point size;

private:
    void save_terminal_size (void)
    {
        int x = 0;
        int y = 0;
#ifndef _WIN32
#ifdef TIOCGSIZE
        struct ttysize win;
#elif defined(TIOCGWINSZ)
        struct winsize win;
#endif
#ifdef TIOCGSIZE
        if (!ioctl(STDOUT_FILENO, TIOCGSIZE, &win)) {
            y = win.ts_lines;
            x = win.ts_cols;
        }
#elif defined TIOCGWINSZ
        if (ioctl(STDOUT_FILENO, TIOCGWINSZ, &win)) {
            return (0);
        }

        y = win.ws_row;
        x = win.ws_col;
#else
        const char *s;
        s = getenv("LINES");
        if (s) {
            y = strtol(s,NULL,10);
        }
        s = getenv("COLUMNS");
        if (s) {
            x = strtol(s,NULL,10);
        }
#endif
#endif
        //
        // Last resort
        //
        if (!x) { x = 80; }
        if (!y) { y = 25; }

        size.x = x;
        size.y = y;
    }
};
#endif
