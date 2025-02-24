x = 5
y = 6
print(x>1 and y<10)
print(x>5 and y<10)

print(x>1 or y<5)
print(x>5 or y<5)

print(not y<10)
print(not x>5)

a = int(input("Enter the number :"))
print((a>0 and a<100) and a%2 ==1 )
print(0<a<100 and a%2 ==1)

x = 5000
y = 5000
print(x is  y)
print(x is not y)

nums = [10,20,23,45,50]
print("10 in a nums :", 10 in nums)
print("10 not in a nums :", 10 not in nums)

x = 5
y = 10
z = x & y
print(z)