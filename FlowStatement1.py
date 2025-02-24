n = 11
if n%2 == 0:
    print("This is a even number")
else:
    print("This is a odd number")

a = 10
if a<0:
    print("This is a negative number")
elif a>0:
    print("This is a positive number") 
else:
    print("This is zero")    

marks = int(input("Enter your marks :"))
if 85<= marks <=100:
    print("A")
elif 75<= marks <85:
    print("B")
elif 65<= marks <75:   
    print("c")
elif 55<= marks <65:   
    print("D")
else:
    print("F")  


if marks >100 or marks <0:
    print("Out of range")
elif marks >= 85:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 65:   
    print("c")
elif  marks >= 55:  
    print("D")
else:
    print("F")   

a = int(input("Enter num1 :"))
b = int(input("Enter num2 :"))
c = int(input("Enter num3 :"))
if a>b:
    print("A Is the largest num")
elif b>c:
    print("B Is the largest num")
else:
    print("C Is the largest num")
    