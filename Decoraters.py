"""
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

def ordinary():
    print("I am ordinary")

get_decorated = make_pretty(ordinary)
get_decorated()
"""
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
def ordinary():
    print("I am ordinary")
ordinary()

"""
write a python programme with folowing requirement 
- create a decorater check positive that 
    - if the input to a function is a positive number
    - if the input is not positive print a message like input must be a positive number 
- use this decorater on a function calulate square root that
    - take one number as input 
    - returns the squre root of the input number 
"""

import math

def check_positive(func):
    def inner(a):
        if a < 0:
            print("Input must be a positive number")
        else:
            return func(a)  # Return the result of the original function
    return inner  # Correctly return the `inner` function

@check_positive
def square_root(num):
    return math.sqrt(num)

print(square_root(16))  # Should print the square root of 16
print(square_root(-4))  # Should print a warning and return None

    