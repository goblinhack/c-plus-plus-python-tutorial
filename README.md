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

Comparison of C++ and Python for lesson 1?
------------------------------------------

In the end, the Python implementation is a bit shorter. The C++ one will run
quicker, but at this point it does not matter. We will deal with performance
later.

C++ is a bit awkward with setting up of vectors of strings as we need to use
C++11 initializer lists. Python is very easy in this regard.

Python you need to avoid using print() as it always adds in newlines, and here
we want raw access to the console, hence sys.stdout.write works nicely.

Escape code stuff
-----------------

All the setup for the escape code sequences is done in a single class Ansi that
you can pull into your code easily. To understand escape code sequences is not
essential, but you'd be mad to not want to know this stuff! [this link](https://stackoverflow.com/questions/4842424/list-of-ansi-color-escape-sequences#4842438) is really good:

Lesson 1 in C++:
-----------------

<pre>
    int main (int argc, char *argv[])
    {
        Ansi ansi;

        std::cout << ansi.get_code(ansi.FOREGROUND_RED);
        std::cout << "hello ";

        std::cout << ansi.get_code(ansi.FOREGROUND_GREEN);
        std::cout << "beautiful";
        std::cout << ansi.get_code(ansi.RESET);

        std::cout << ansi.get_code(ansi.FOREGROUND_CYAN);
        std::cout << " colorful";
        std::cout << ansi.get_code(ansi.RESET);

        std::cout << ansi.get_code(ansi.FOREGROUND_BLUE);
        std::cout << " world";
        std::cout << ansi.get_code(ansi.RESET);
        std::cout << std::endl;

        return (0);
    }
</pre>

Lesson 1 in Python:
-------------------

<pre>
    def lesson1():
        """ hello beautiful world """
        ansi = Ansi()
    
        for bg_col in range(ansi.Code.BACKGROUND_BLACK,
                            ansi.Code.BACKGROUND_WHITE):
            for fg_col in range(ansi.Code.FOREGROUND_BLACK,
                                ansi.Code.FOREGROUND_WHITE):
                sys.stdout.write("{0: <20} {1: <20}".format(\
                                 ansi.get_code_name(bg_col),
                                 ansi.get_code_name(fg_col)))
                sys.stdout.write(ansi.get_bgfg_code(bg_col, fg_col))
                sys.stdout.write("colorful")
                sys.stdout.write(ansi.get_code(ansi.Code.RESET))
                print()
    
        sys.stdout.write(ansi.get_code(ansi.Code.FOREGROUND_RED))
        sys.stdout.write("hello")
    
        sys.stdout.write(ansi.get_code(ansi.Code.FOREGROUND_GREEN))
        sys.stdout.write(" beautiful")
    
        sys.stdout.write(ansi.get_code(ansi.Code.FOREGROUND_CYAN))
        sys.stdout.write(" colorful")
    
        sys.stdout.write(ansi.get_code(ansi.Code.FOREGROUND_BLUE))
        sys.stdout.write(" world")
    
        sys.stdout.write(ansi.get_code(ansi.Code.RESET))
        print("from Python")
    
    lesson1()
</pre>

Building
--------

To build and run (all) examples, try the following:

![Alt text](lesson1/screenshot2.png?raw=true "hello colorful world")


Lesson 2: Getting the terminal info
===================================

Before we can do anything more advanced we need to know the terminal size.
So we do that here, but also add in some more concepts:

C++
---
- template class (point.h)
- class inheritance (Terminal inherits Ansi class)
- header files, we've split ansi and terminal code out to their own modules
- some ioctl() ickyness for getting the terminal size
- std::ostream& operator << for classes so they can print themselves
- class operators

Python
------
- class inheritance (Terminal inherits Ansi class)
- modules, we've split ansi and terminal code out to their own modules
- python is much cleaner at getting the terminal size here than C++
- \_\_str\_\_ methods for classes so they can print themselves

Comparison of C++ and Python for lesson 2?
------------------------------------------

Python is still making it easier. Wrapping the system calls to get the
terminal size is a no brainer in python and horrible in C++. C++ remains
my favorite language, but we'll see how this progresses.

Building
--------

![Alt text](lesson2/screenshot.png?raw=true "hello colorful world")

Lesson 3
========

TODO drawing lines

Lesson 4
========

TODO frame buffer

Lesson 5
========

TODO keyboard input

Lesson 6
========

TODO moving a shape around the screen
