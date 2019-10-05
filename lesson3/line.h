#ifndef LINE_H
#define LINE_H

#include <list>
#include "point.h"
#include "terminal.h"

class Line {
public:
    //
    // The points that comprise the line
    //
    std::list<Point> points;

    //
    // Where to draw to
    //
    Terminal *terminal {};

    Line (Terminal *term, Point a, Point b)
    {
        terminal = term;

        float slope = 100.0;
        float x0 = a.x;
        float y0 = a.y;
        float x1 = b.x;
        float y1 = b.y;

        if (x0 != x1) {
            slope = (y1 - y0) * (1.0 / (x1 - x0));
        }

        if ((0 <= slope) && (slope <= 1)) {
            draw_line_segment(Point(x0, y0), Point(x1, y1), 0);
        } else if ((-1 <= slope) && (slope <= 0)) {
            draw_line_segment(Point(x0, -y0), Point(x1, -y1), 3);
        } else if (slope > 1) {
            draw_line_segment(Point(y0, x0), Point(y1, x1), 1);
        } else {
            draw_line_segment(Point(-y0, x0), Point(-y1, x1), 2);
        }
    }

    void draw (char c)
    {
        for (auto p : points) {
            terminal->set_cursor(Point(p.x, p.y));
            std::cout << c;
        }
    }

private:
    void draw_line_segment (Point a, Point b, int flag)
    {
        float temp;
        float dx;
        float dy;
        float tdy;
        float dydx;
        float p;
        float x;
        float y;
        float i;

        float x0 = a.x;
        float y0 = a.y;
        float x1 = b.x;
        float y1 = b.y;

        if (x0 > x1) {
            temp = x0;
            x0 = x1;
            x1 = temp;

            temp = y0;
            y0 = y1;
            y1 = temp;
        }

        dx = x1 - x0;
        dy = y1 - y0;

        tdy = 2.0 * dy;
        dydx = tdy - (2.0 * dx);

        p = tdy - dx;
        x = x0;
        y = y0;

        if (flag == 0) {
            points.push_back(Point(x, y));
        } else if (flag == 1) {
            points.push_back(Point(y, x));
        } else if (flag == 2) {
            points.push_back(Point(y, -x));
        } else if (flag == 3) {
            points.push_back(Point(x, -y));
        }

        for (i = 1; i <= dx; i++){
            x++;

            if (p < 0) {
                p += tdy;
            } else {
                p += dydx;
                y++;
            }

            if (flag == 0) {
                points.push_back(Point(x, y));
            } else if (flag == 1) {
                points.push_back(Point(y, x));
            } else if (flag == 2) {
                points.push_back(Point(y, -x));
            } else if (flag == 3) {
                points.push_back(Point(x, -y));
            }
        }
    }
};
#endif
