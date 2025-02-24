#Dedault arguments - eka para ekaka initially assign krla eka para ekak withrak pass krnna pluwn
def add_num(a,b=5):
    return a+b
print(add_num(6))

"""
if you have default parameter all default parameter should be in the right side of the parathesis
 This will be error
def add_num(a,b=5,c):
    return a+b+c
"""
def add_num(a,b,c=5):
    return a+b+c
print(add_num(2,3))

#Positional argument
#values are pased in a order a will be 7 and b will be 9
def add_num(a,b):
    return a+b
print(add_num(7,9))

#Keyword arguments
#When you send arguments like this order doesnt matter anymore
def add_num(a,b):
    return a+b
print(add_num(a=7,b=7))

"""
define a function to calculate _total cost with following parameters (item price:mandatory , quntity:mandatory ,
discount:optional (a percentage applied to the total price)default should be 0 , tax:optional (a percentage applied to the discounted price)
"""


def  cal_total(item1,item2,item3):
    return  item1+item2+item3 
total = (cal_total(200,300,400))
print("Total is : " ,total)

def cal_disc(total,discount):
    return total-total*discount/100
discounted_total= (cal_disc(total,10))
print("Discounted Total : " ,discounted_total)

def cal_tax(discounted_total,tax_rate):
    return discounted_total-discounted_total*tax_rate/100
final_total= (cal_tax(discounted_total,5))
print("Final Total : ",final_total)

"""
def calculate_total(price, quantity, discount=0, tax=0):
    total_price = price * quantity  # Multiply price and quantity to get the total price
    discounted_amount = total_price * discount / 100  # Calculate the discount amount
    discounted_price = total_price - discounted_amount  # Apply the discount to get the discounted price
    tax_amount = discounted_price * tax / 100  # Calculate the tax amount on the discounted price
    final_amount = discounted_price + tax_amount  # Add tax to the discounted price
    return final_amount
"""

#Aribitrary positional arguments
"""
pass krnna one argument type eka dn naththn one thrn argument one wdihata pass krnna pluwn eka tuple ekak wdihta thma store wenne 
"""
def arbitory_positional_argument(*args):
    print(args,type(args))
arbitory_positional_argument(1,2,3)

#calculate the sumation of passing numbers 
def cal_sum(*numbers):
    sum = 0
    for num in numbers: #num kiyna temory varuable eka api pass krna numbers wla thinynwad kiyl check krnnawa thiynwa nm eka sum ekata add krnwa 
        sum += num
    return sum

print(cal_sum(1,2,3,4,5))

#summerize grades that accept that student name as mandetory argument and an aribitrary num of grade scores the function should,
#print the student names
#calculate and print the highest grade, lowest and avg from the provided scores
#if no grades are provided you print no grades available

def cal_grades(name, *grades):
    print("Student Name: " + name)
    if not grades:  # Check if grades are provided
        print("Grades not available")
    else:
        print("Highest Grade: ", max(grades))  # Find the highest grade
        print("Lowest Grade: ", min(grades))   # Find the lowest grade

        # Calculate the total of grades
        total = sum(grades)
        print("Sum of Grades: ", total)

        return total  # Return the sum of grades

# Example usage
print(cal_grades("Jana", 23, 45, 56))



#Arbitrary keyword arguments(**kwargs) - dictonary ekak krla ewanne

    
#Employee mng system 
#employee_info that accept reqired name parameter and arbitrary num of keyword arguments representing additional details about the employee the function should,
#print the employees name
#iterate through the keyword arguments and print each key value pairs in the format "<key>:<value>"
#return a dictionary with all the employee details
"""
def employee_info(name,**data):
    print("Employee Name: ",name)
    for key,value in data.items():
        print(key ,":",value)
        return{"name":name}|data
        return{"name":name,**data}
        result = employee_info(name,**data)
        print(result)
employee_info(name="tharu",age=23,city="nuwara")
"""
def employee_info(name, **data):
    print("Employee Name:", name)
    for key, value in data.items():
        print(key, ":", value)
    # Return a merged dictionary with "name" and other key-value pairs
    return {"name": name, **data}

# Call the function and store the result
result = employee_info(name="tharu", age=23, city="nuwara")
# Print the returned dictionary
print(result)


