#Nested Function
def outer(x):
    def inner(y):
        return x+y
    return inner

temp_value = outer(5)
print(temp_value(7))

#Function as a argument
def add(x,y):
    return x+y
def calculate(func,x,y):
    return func(x,y)
result = calculate(add,4,6)
print(result)
