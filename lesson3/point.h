//
// Template class implementing an integer Point
//
#ifndef POINT_H
#define POINT_H
#include <cmath>

template <class S> S squared (S a) { return a * a; }

template<class T> class my_aPoint
{
public:
    T x {};
    T y {};

    my_aPoint (void) : x(0), y(0) {};

    my_aPoint (T x, T y) : x(x), y(y) { }

    my_aPoint (const my_aPoint &a) : x(a.x), y(a.y) { }

    friend std::ostream& operator << (std::ostream &out, const my_aPoint &my)
    {
        out << "(" << my.x << ", " << my.y << ")";
        return (out);
    }

    void operator+= (my_aPoint a)
    {
        x += a.x; y += a.y;
    }

    void operator-= (my_aPoint a)
    {
        x -= a.x; y -= a.y;
    }

    void operator/= (my_aPoint a)
    {
        x /= a.x; y /= a.y;
    }

    void operator*= (my_aPoint a)
    {
        x *= a.x; y *= a.y;
    }

    void operator*= (T a)
    {
        x *= a; y *= a;
    }

    void operator/= (T a)
    {
        x /= a; y /= a;
    }

    friend my_aPoint operator+ (my_aPoint a, my_aPoint b)
    {
        return (my_aPoint(a.x + b.x, a.y + b.y));
    }

    friend my_aPoint operator- (my_aPoint a, my_aPoint b)
    {
        return (my_aPoint(a.x - b.x, a.y - b.y));
    }

    friend my_aPoint operator/ (my_aPoint a, my_aPoint b)
    {
        return (my_aPoint(a.x / b.x, a.y / b.y));
    }

    friend my_aPoint operator/ (my_aPoint a, T b)
    {
        return (my_aPoint(a.x / b, a.y / b));
    }

    friend my_aPoint operator* (my_aPoint a, T b)
    {
        return (my_aPoint(a.x * b, a.y * b));
    }

    friend my_aPoint operator* (my_aPoint a, my_aPoint b)
    {
        return (my_aPoint(a.x * b.x, a.y * b.y));
    }

    friend bool operator== (my_aPoint a, my_aPoint b)
    {
        return (a.x == b.x) && (a.y == b.y);
    }

    friend bool operator!= (my_aPoint a, my_aPoint b)
    {
        return (!(a==b));
    }

    friend T distance (my_aPoint a, my_aPoint b)
    {
        return (T) sqrt((double)(squared((b.x)-(a.x))+squared((b.y)-(a.y))));
    }

    T length (void) const
    {
        return (sqrt(x*x + y*y));
    }

    void unit (void)
    {
        T length = sqrt(x*x + y*y);

        x /= length;
        y /= length;
    }
};

typedef my_aPoint<int> Point;
#endif
