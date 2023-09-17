import turtle
import math
import time


def square(t, length):
    t = turtle.Turtle()
    for i in range(4):
        t.fd(length)
        t.lt(90)
    turtle.mainloop()

def polygon(t, length, n):
    t = turtle.Turtle()
    angle = 360.0 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)
    turtle.mainloop()
    
def circle(t, r):
    t = turtle.Turtle()
    circumference = 2 * math.pi * r
    n = 30
    length = circumference / n
    polygon(t, length, n)
    turtle.mainloop()

# circle('bob',80)


from time import time, ctime
t = time()
# print('\n', "Today's time and date is:", ctime(t),'\n')
# print("There has been",t // 86400, "days since the epoch!")

# Fermat's Last Theorem
def check_fermat(a, b, c, n):
    if n <= 2:
        input('Error! "n" needs to be greater than 2!')
    elif a**n + b**n == c**n:
        print('Holy smokes, Fermat was wrong!')
    elif a**n + b**n != c**n:
        print("No, that doesn't work.")

# check_fermat(1, 2, 2, 1)

# Fruitful functions
def compare(x, y):
    if x == y:
        return 0
    elif x > y:
        return 1
    else:
        return -1
result = compare(5,3) 
# print(result), Output will be 1.



