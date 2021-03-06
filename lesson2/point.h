//
// Template class implementing an integer point
//
#ifndef POINT_H
#define POINT_H
#include <cmath>

template <class S> S squared (S a) { return a * a; }

template<class T> class my_apoint
{
public:
    T x {};
    T y {};

    my_apoint (void) : x(0), y(0) {};

    my_apoint (T x, T y) : x(x), y(y) { }

    my_apoint (const my_apoint &a) : x(a.x), y(a.y) { }

    friend std::ostream& operator << (std::ostream &out, const my_apoint &my)
    {
        out << "(" << my.x << ", " << my.y << ")";
        return (out);
    }

    void operator+= (my_apoint a)
    {
        x += a.x; y += a.y;
    }

    void operator-= (my_apoint a)
    {
        x -= a.x; y -= a.y;
    }

    void operator/= (my_apoint a)
    {
        x /= a.x; y /= a.y;
    }

    void operator*= (my_apoint a)
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

    friend my_apoint operator+ (my_apoint a, my_apoint b)
    {
        return (my_apoint(a.x + b.x, a.y + b.y));
    }

    friend my_apoint operator- (my_apoint a, my_apoint b)
    {
        return (my_apoint(a.x - b.x, a.y - b.y));
    }

    friend my_apoint operator/ (my_apoint a, my_apoint b)
    {
        return (my_apoint(a.x / b.x, a.y / b.y));
    }

    friend my_apoint operator/ (my_apoint a, T b)
    {
        return (my_apoint(a.x / b, a.y / b));
    }

    friend my_apoint operator* (my_apoint a, T b)
    {
        return (my_apoint(a.x * b, a.y * b));
    }

    friend my_apoint operator* (my_apoint a, my_apoint b)
    {
        return (my_apoint(a.x * b.x, a.y * b.y));
    }

    friend bool operator== (my_apoint a, my_apoint b)
    {
        return (a.x == b.x) && (a.y == b.y);
    }

    friend bool operator!= (my_apoint a, my_apoint b)
    {
        return (!(a==b));
    }

    friend T distance (my_apoint a, my_apoint b)
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

typedef my_apoint<int> point;
#endif
