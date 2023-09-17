def do_twice(f, Value):
    f(Value)
    f(Value)

def print_twice(bruce):
    print(bruce)
    print(bruce)

# do_twice(print_twice,"spam")

def do_four(f, Value):
    f(f(Value))
    f(f(Value))

# do_four(print_twice,"spam")

def court_grid():
    print('+', '-', '-', '-', '-', '+', '-', '-', '-', '-', '+')
    print('|', '\t ', '|', ' \t ', '  |')
    print('|', '\t ', '|', ' \t ', '  |')
    print('|', '\t ', '|', ' \t ', '  |')
    print('|', '\t ', '|', ' \t ', '  |')
    print('+', '-', '-', '-', '-', '+', '-', '-', '-', '-', '+')
    print('|', '\t ', '|', ' \t ', '  |')
    print('|', '\t ', '|', ' \t ', '  |')
    print('|', '\t ', '|', ' \t ', '  |')
    print('|', '\t ', '|', ' \t ', '  |')
    print('+', '-', '-', '-', '-', '+', '-', '-', '-', '-', '+')

# court_grid()

import turtle
bob = turtle.Turtle()
