# this is a test comment

import math


def square_root(a):
    if a < 0:
        raise ValueError
    math.sqrt(a)# raise ValueError if a < 0
def hypotenuse(a, b):
    math.hypot(a, b) # can have negative nums


def add(a, b):
    return (a + b)

def sub(a, b):
    return (a - b)

def mul(a, b):
    return (a * b)

def log(a, b):
    if a <= 0 or a == 1 or b<= 0:
        raise ValueError
    return (math.log(b)/ math.log(a))
    # use math library + raise ValueError

def exp(a, b):
    return(a**b)
