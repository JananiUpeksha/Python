"""
#import my_module as md
from my_module import add #from my_module import * but this is not a good practise 
import math
#print(md.add(3,5))
print(add(3,5))
print(math.pi)
print(math.factorial(10))
"""

#main.py
#import the entire module
import my_calculator.addition
import my_calculator.substraction

result1 = my_calculator.addition.add(20,20)
result2 = my_calculator.substraction.sub(100,50)

print(result1)
print(result2)