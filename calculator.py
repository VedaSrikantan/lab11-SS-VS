# https://github.com/VedaSrikantan/lab11-SS-VS.git
# Partner 1: Sarah Spellman
# Partner 2: Veda Srikantan

import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
   return a*b
def div(a,b):
    if a ==0:
        raise ZeroDivisionError
    else:
        return b/a
def log(a,b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError
    return math.log(b, a)
def exp(a,b):
    return a**b
def square_root(a):
    if a<0:
        raise ValueError
    return math.sqrt(a)
def hypotenuse(a,b):
    return math.hypot(a,b)