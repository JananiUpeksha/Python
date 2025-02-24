#List & Tuple unpacking
my_list = [8,10,12]
x,y,z = my_list
print(x,y,z)

my_tuple = (10,20,30)
a,b,c = my_tuple
print(a,b,c)

#Dictionary unpacking
person = {"name": "Jana","age": 24,}
# Unpacking using variable assignment
name = person["name"]
age = person["age"]
print(name, age)

# OR, if you want dictionary unpacking directly
name, age = person["name"], person["age"]
print(name, age)

# OR, using for loop
for key,value in person.items():
    print(key,value)

#Extract only keys
for key in person.keys():
    print(key)

#Extract only values
for value in person.values():
    print(value)