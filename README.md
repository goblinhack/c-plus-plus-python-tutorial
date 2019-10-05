About
=====

Tired of boring examples in how to program? Of course you are! This little
series aims to begin at something a bit more interesting than "hello world"
and end up with a fun little demo. At all stages we will have the same demo
written in C++ and then Python for comparison of the two languages. 

I will avoid use of external libraries, so things like writing colours to
the console will be less portable than useing Curses, but will be more fun
and educational.

Hello Colorful World
====================

Let's begin with printing a colorful message to the console. You will need
something that supports ANSI escape sequences. Most terminals should do the
job. 

Here's how it will look in C++ and Python:

![Alt text](lesson1/screenshot.png?raw=true "hello colorful world")

Ignoring all the code for setting up the ANSII escape code sequences, in
the end it is quite simple.

- ![#f03c15](https://placehold.it/15/f03c15/000000?text) `#f03c15` c++

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

Python:

<pre>
    TBD
</pre>

Building
========

To build and run the examples, hopefully this should be all you need.

<pre>
    sh ./RUNME
</pre>
