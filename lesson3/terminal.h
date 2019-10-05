#ifndef TERMINAL_H
#define TERMINAL_H
//
// Terminal routines, like get the size
//

#ifndef _WIN32
#include <sys/ioctl.h>
#include <termios.h>
#include <unistd.h> // for STDOUT_FILENO
#endif

//
// A template class describing a 2d Point
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

        //
        // Save the jump codes for moving the cursor
        //
        save_cursor_codes();
    }

    Point size;
    
    void set_cursor (Point p)
    {
        assert((p.x >= 0) && (p.x < size.x));
        assert((p.y >= 0) && (p.y < size.y));
        std::cout << cursor_codes[p.x][p.y];
    }

    void cls (void)
    {
        set_cursor(Point(0, 0));
        std::cout << "\033[2J";
    }

    void bottom_left (void)
    {
        set_cursor(Point(0, size.y-1));
    }

    void bottom_right (void)
    {
        set_cursor(Point(size.x-1, size.y-1));
    }

    void top_left (void)
    {
        set_cursor(Point(0, 0));
    }

    void top_right (void)
    {
        set_cursor(Point(size.x-1, 0));
    }

private:
    void save_cursor_codes (void)
    {
        for (auto x = 0; x < size.x; x++) {
            cursor_codes.resize(size.x);
            for (auto y = 0; y < size.y; y++) {
                cursor_codes[x].resize(size.y);
            }
        }

        for (auto x = 0; x < size.x; x++) {
            auto xs = std::to_string(x);
            for (auto y = 0; y < size.y; y++) {
                auto ys = std::to_string(y);
                cursor_codes[x][y] = "\033[" + ys + ";" + xs + "H";
            }
        }
    }

private:
    std::vector< std::vector< std::string> > cursor_codes;

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
