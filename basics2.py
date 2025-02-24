my_list = [1,2,2,"cat",3,4,5]
my_list1 = my_list
print(my_list1)#not cping just assigning the same if we change my_list same will affect to my_list1

my_list1 = my_list.copy()#this will copy my list to my list 1 but changes in my list will not affect to my list1
my_list[1] = 35
print(my_list , my_list1)

my_list1 = list(my_list)#using list constructor work same as copy()
my_list[3] = "dog"
print(my_list , my_list1)

my_list2 = my_list + my_list1 #work same as ectend method concat 2 arrays
print(my_list2,len(my_list2))

