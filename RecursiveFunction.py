def find_factorial(n):
    if n == 0:
        return 1
    factorial = 1  # Initialize factorial inside the function
    for i in range(1, n + 1):
        factorial *= i
    return factorial

n = 3
result = find_factorial(n)
print(f"The factorial of {n} is {result}")


#as a recursive function
def factorial(x):
    if x==0 or x==1:
        return 1
    else:
        return(x*factorial(x-1))
n = 10
result = factorial(n)
print(f"The factorial of {n} is {result}")
#1000n psse error enwa the maximum depth of recursion is 100 if the limit is crossed it result in recursionError

#take list and return the sum of list as a recursion
my_list = [1,2,3,4,5]
length = len(my_list)
print(length)

def find_sum(length):
    if length>0 :
        return 0
    else:
        return
def resursice_sum(:ki)


















