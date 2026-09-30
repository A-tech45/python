# the *args takes all the listed values 
"""
In Python, *args lets a function accept any number of positional arguments.

Without *args
def add(a, b):
    return a + b

add(2, 3)

This function expects exactly 2 arguments.

With *args
^ def add(*args):
^    print(args)

^ add(2, 3, 4, 5)

^ Output:

^ (2, 3, 4, 5)

^ args becomes a tuple containing all the arguments.

You can loop through it:

def add(*args):
    total = 0

    for num in args:
        total += num

    return total

print(add(2, 3, 4, 5))

Output:

14
The important idea
add(2, 3, 4, 5)
       ↓
     *args
       ↓
(2, 3, 4, 5)

The * essentially means "collect all extra positional arguments into one variable."

And args isn't a special keyword—you could technically write:

def add(*numbers):

*args is simply the conventional name.
"""

def sum_all (*args):
   for i in args :
    print(i)
    
    

sum_all(3 , 2 , 5 , 6)