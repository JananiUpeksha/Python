"""
def function_name(parameters):
    #Body of statement
    return expresion
"""
def calculate_sum(a,b):
    return  a+b
def send_num():
    result = calculate_sum(2,3)
    print(result)
send_num()


def calculate_sum(a,b):
    return  a+b
print(calculate_sum(4,6))


"""
def area_of_circle(r):
    return 22/7*r*r
print(area_of_circle(7))
"""

PI_VALUE = 3.14
def area_of_circle(r):
    return PI_VALUE*r*r
print(area_of_circle(7))


my_list = [2, 3, 4, 6, 5, 9]
def find_mean(list1):
    total = 0  
    for x in list1:
        total += x
    mean = total / len(list1)  
    return mean  

mean_value = find_mean(my_list)
print("Mean of the list:", mean_value)

mylist = [2,4,3,6,9,8,5]
print(mylist[1:5:1])
print(mylist[1:5:2])
print( : :2)



