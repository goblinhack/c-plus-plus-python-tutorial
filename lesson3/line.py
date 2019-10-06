
import sys
from point import Point
from terminal import Terminal

class Line:
    def __init__(self, term, a, b):
        self.terminal = term
        self.points = []

        slope = 100.0
        x0 = a.x
        y0 = a.y
        x1 = b.x
        y1 = b.y

        if x0 != x1:
            slope = (y1 - y0) * (1.0 / (x1 - x0))

        if (0 <= slope) and (slope <= 1):
            self.draw_line_segment(Point(x0, y0), Point(x1, y1), 0)
        elif (-1 <= slope) and (slope <= 0):
            self.draw_line_segment(Point(x0, -y0), Point(x1, -y1), 3)
        elif slope > 1:
            self.draw_line_segment(Point(y0, x0), Point(y1, x1), 1)
        else:
            self.draw_line_segment(Point(-y0, x0), Point(-y1, x1), 2)

    def draw(self, c):
        for p in self.points:
            self.terminal.set_cursor(Point(p.x, p.y))
            sys.stdout.write(c)

    def draw_line_segment(self, a, b, flag):
        x0 = a.x
        y0 = a.y
        x1 = b.x
        y1 = b.y

        if (x0 > x1):
            temp = x0
            x0 = x1
            x1 = temp

            temp = y0
            y0 = y1
            y1 = temp

        dx = x1 - x0
        dy = y1 - y0

        tdy = 2.0 * dy
        dydx = tdy - (2.0 * dx)

        p = tdy - dx
        x = x0
        y = y0

        if flag == 0:
            self.points.append(Point(x, y))
        elif flag == 1:
            self.points.append(Point(y, x))
        elif flag == 2:
            self.points.append(Point(y, -x))
        elif flag == 3:
            self.points.append(Point(x, -y))

        for i in range(1, dx+1):
            x+=1

            if p < 0:
                p += tdy
            else:
                p += dydx
                y+=1

            if flag == 0:
                self.points.append(Point(x, y))
            elif flag == 1:
                self.points.append(Point(y, x))
            elif flag == 2:
                self.points.append(Point(y, -x))
            elif flag == 3:
                self.points.append(Point(x, -y))
