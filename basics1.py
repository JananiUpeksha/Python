a = 200
print (a)
print ("The type of variable having value", a , "is" , type(a))


num_1 = 2.5e4
print(num_1 , type(num_1))

#Casting
num_1 = 5
num_2 = 12.5
a = float(num_1)
print (a,type(a))
b = int(num_2)
print (b,type(b))

my_list = [1,13,24,56,78]
print(my_list , type(my_list))
print(my_list[2])
my_list[2] = 44
print(my_list)
my_list1 = [1,"Janani",24,56,78,True]
print(my_list1)
my_list2 = [1,13,24,56,78,13]
print(my_list2)
print(len(my_list2))
print(my_list2[-1])
print(my_list2[-2])
print(my_list2[1:5])
print(my_list2[:3])
print(my_list2[2:])
my_list3 = [1,"cat",24,69,78,True]
my_list3[1:3] = ["dog",18.9]
print(my_list3)

#Add new --> there are 2 methods
my_list3 = [1,"cat",24,69,78,True]
my_list3.insert(3,"rabit")
print(my_list3 ,"Length is " , len(my_list3))

my_list3.append("car")
print(my_list3 ,"Length is " , len(my_list3))
new_list = ["bus",False,17]

#Add an array
my_list3.extend(new_list)
print(my_list3 ,"Length is " , len(my_list3))

#Remove from specific position
my_list3.pop(2)
print(my_list3 ,"Length is " , len(my_list3))
del my_list3[2]
print(my_list3 ,"Length is " , len(my_list3))
del my_list3 #to destroy the whole array - no out put if it print there will be a error
my_list2.clear()
print(len(my_list2))#output will dis nplay as a 0

#Sorting algorithms
list1 = ["cat","dog","dear","eagle"]
list1.sort() #case sensitive sort , it will give piority to upper letters
print(list1)
list1 = ["cat","Dog","dear","eagle"]
list1.sort(key=str.lower)#ignore upper letter piority and make according to alphebetical order 
print(list1)
list1 = ["cat","dog","Dear","eagle"]
list1.sort(reverse = True)#in decending order
print(list1)
list1 = ["cat","dog","Dear","eagle"]
list1.reverse()#Just twist the side of the original array
print(list1)

#Task
myList1 = [-10,-18,12,5,7,12,-3]
myList2 = [8,4,-3,9,2,11]
myList1.extend(myList2)
print(myList1)
myList1.sort()
print(myList1)

position_of_median = (len(myList1)+1)/2
position_of_median = int(position_of_median)
print(position_of_median)
median = myList1[position_of_median-1]
print(median)

position_of_q1 = (len(myList1)+1)/4
position_of_q1 = int(position_of_q1)
print(position_of_q1)
value_q1 = (myList1[position_of_q1-1] + myList1[position_of_q1])/2

position_of_q3 = 3* (len(myList1)+1)/4
position_of_q3 = int(position_of_q3 )
value_q3 = (myList1[position_of_q3-1] + myList1[position_of_q3])/2
print(value_q3)
