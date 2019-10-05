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

C++:

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

To build and run the examples, try the following:

![Alt text](lesson1/screenshot2.png?raw=true "hello colorful world")

