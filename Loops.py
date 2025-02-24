# for item in sequence:
# item - Tempaty variable that hold the value of seqence

fruits = ["apple","banana","mango"]
for fruit in fruits:
    print(fruit)

my_list = [1,2,3,4,5]
squre_list = []
for num in my_list:
    squre_list.append(num**2)
    print(squre_list)

#List Comprehensive
#expression in the value that gets added to the list
#item is the curent element from the iterable
#if condision is optional and filters elements
squre_list = [num**2 for num in my_list]
print("Squre List :", squre_list)

new_list1 = [1,2,3,4,5,6,7,8,9,10]
new_list2 = [num**2 for num in new_list1]
print(new_list2)
new_list3 = [num**2 for num in range(1,11)]
print(new_list3)

new_list4 = [num**2 for num in range(1,11) if num%2 == 0]
#new_list4 = [num**2 for num in range(2,11,2)]
print(new_list4)

m = 5
i = 0
while i < m:
    print(i, end = " ")
    i = i+1
print("END")

x = int(input("Enter the prefered end number : "))
y = 2
while y<x:
    print(y)
    y+=2

#Break condition
x = int(input("Enter the preferred end number: "))
y = 2
while y < x:
    if y == 10:
        break
    else:
        print(y)
    y += 2

total = 0
while True:
    x = int(input("Enter the number :- "))
    if x == 0:
        break
    else:
        total += x
print("Total is : ",total)

#continue - to print odd nums(ignore even)
my_list = [3,8,15,10,9,7,14]
for nums in my_list:
    if nums %2 == 0:
        continue
    else:
        print(nums)

  



    