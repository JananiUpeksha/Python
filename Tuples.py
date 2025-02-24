my_tuple1  = (12,"DOG",10)
print(len(my_tuple1))
# my_tuple1[1] = "rat" # 'tuple' object does not support item assignment
print(my_tuple1[1]) #Tuples are unchangable

#But there is a way to change the tuple
my_tuple1  = (12,"DOG",10)
# 1st change tuple into list
my_list1  = list(my_tuple1)
# 2nd do whatever changers need to do
my_list1[1] = "rat"
# 3rd convert list back to tuple
my_tuple1 = tuple(my_list1)
print(my_tuple1, type(my_tuple1))

#Excersice1
#Remove 3rd element from 1st tuple then create 1 using both tuples then sort
my_tuple_1 = (10,8,20,5)
my_tuple_2 = (5,9,-1)
# Convert into list
my_list_1 = list(my_tuple_1)
my_list_2 = list(my_tuple_2)

my_list_1.pop(2) # remoce 1st element
my_list_1.extend(my_list_2) # concat to 1 list
my_list_1.sort() # then sort
print(my_list_1)

my_tuple_1 = tuple(my_list_1)
print(my_tuple_1 )






