#absolute value
abs(-20)

#map() - apply given function to every item in the iterable and return an iterator that contain the results
# 1st para will be user define function,2nd iterable(list,tuple or..) me 2 ka pass klama function eka e list eka athule iterate wenwa
#eke return type eka <class"map"> eka wens krna one nm list ekak krla wens krnna e dewal krnna pluwn
def find_square(x):
    return x*x

my_list = [5,4,2]
result = map(find_square,my_list)
print(result,type(result))
result = list(result)
print(result,type(result))

#map(function,iterable,iterable,iterable) - iterable one thrmak pass krnna pluwn
my_list1 = [10, 12, 7, 5]
my_list2 = [9, 5, 4, 1]

# Function to find the summation of two numbers
def find_summation(num1, num2):
    return num1 + num2

# Use map to sum corresponding items from both lists
summation = map(find_summation, my_list1, my_list2)

# Convert the map object to a list
summation_list = list(summation)

# Print the resulting list
print(summation_list)

#u have list of integers represnting tempresures in celcius tempreture_sequal[20,30,25,40,50]
#use map to convert these tempresure into paranhight use the formula (Fahrenheit = celsius*9/5 + 32)
# List of temperatures in Celsius
temperature_sequence = [20, 30, 25, 40, 50]
def convert(celsius):
    return celsius * 9 / 5 + 32

conversion = map(convert, temperature_sequence)
conversion_list = list(conversion)
print(conversion_list)

#filter(function(should return a logical value),iterable) - return type eka logical true
my_list3 = [5,7,8,3,12,14]
def filter(num):
    return num%2 ==0

odd = map(filter, my_list3)
odd_list = list(odd)
print(odd_list,type(odd_list))

