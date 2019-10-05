About
=====

Tired of boring examples in how to program? Of course you are! This little
series aims to begin at something a bit more interesting than "hello world"
and end up with a fun little demo. At all stages we will have the same demo
written in C++ and then Python for comparison of the two languages. 

I will avoid use of external libraries, so things like writing colours to
the console will be less portable than useing Curses, but will be more fun
and educational.

Lesson 1: Hello Colorful World
==============================

Let's begin with printing a colorful message to the console. You will need
something that supports ANSI escape sequences. Most terminals should do the
job. 

Here's how it will look in C++ and Python:

![Alt text](lesson1/screenshot.png?raw=true "hello colorful world")

This lesson will incorporate quite a lot of ideas:

C++
---
- Classes
- Enums
- Vectors
- Initializer lists (you need C++ 11 for this)
- Writing to the console
- Asserts
- Colors!

Python
------
- Classes
- Enums
- Lists in Python (really in the backed, they are implemented as arrays)
- Writing to the console
- Asserts
- Colors!

Comparison of the C++ and Python?
---------------------------------

In the end, the Python implementation is a bit shorter. The C++ one will run
quicker, but at this point it does not matter. We will deal with performance
later.

C++ is a bit awkward with setting up of vectors of strings as we need to use
C++11 initializer lists. Python is very easy in this regard.

Python you need to avoid using print() as it always adds in newlines, and here
we want raw access to the console, hence sys.stdout.write works nicely.

Escape code stuff
-----------------

All the setup for the escape code sequences is done in a single class Ansii that
you can pull into your code easily. To understand escape code sequences is not
essential, but you'd be mad to not want to know this stuff! This link is really
good:

[this link](https://stackoverflow.com/questions/4842424/list-of-ansi-color-escape-sequences#4842438)

Lesson 1 C++:
-------------

<pre>
    int main (int argc, char *argv[])
    {
        Ansii ansii;

        std::cout << ansii.get_code(ansii.FOREGROUND_RED);
        std::cout << "hello ";

        std::cout << ansii.get_code(ansii.FOREGROUND_GREEN);
        std::cout << "beautiful";
        std::cout << ansii.get_code(ansii.RESET);

        std::cout << ansii.get_code(ansii.FOREGROUND_CYAN);
        std::cout << " colorful";
        std::cout << ansii.get_code(ansii.RESET);

        std::cout << ansii.get_code(ansii.FOREGROUND_BLUE);
        std::cout << " world";
        std::cout << ansii.get_code(ansii.RESET);
        std::cout << std::endl;

        return (0);
    }
</pre>

Lesson 1 Python:
----------------

<pre>
    def lesson1():
        """ hello beautiful world """
        ansii = Ansii()
    
        for bg_col in range(ansii.Code.BACKGROUND_BLACK,
                            ansii.Code.BACKGROUND_WHITE):
            for fg_col in range(ansii.Code.FOREGROUND_BLACK,
                                ansii.Code.FOREGROUND_WHITE):
                sys.stdout.write("{0: <20} {1: <20}".format(\
                                 ansii.get_code_name(bg_col),
                                 ansii.get_code_name(fg_col)))
                sys.stdout.write(ansii.get_bgfg_code(bg_col, fg_col))
                sys.stdout.write("colorful")
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
        print("from Python")
    
    lesson1()
</pre>

Lesson 2: Drawing lines
=======================

Stay tuned!

Building
========

To build and run all examples, try the following:

![Alt text](lesson1/screenshot2.png?raw=true "hello colorful world")

