x = int(input('Enter the number :'))
#result = "OK" if (x%3 == 0 and x%2 == 0) else "NOT OK" 
result = "OK" if (x%6 == 0) else "NOT OK"
print(result)

response_code = 404
match response_code:
    case 200:
        print("OK")
    case 201:
        print("CREATED")   
    case 404:
        print("404 NOT FOUND")
    case 500:
        print("INTERNAL SERVER ERROR")
    case _:
        print("SOMETHING ELSE")

y = int(input('Enter the number :'))
match y:
    case 0:
        print("Zero")
    case -1:
        print("Negative One")
    case 1:
        print("Positive One")
    case _ if y>1:
    #case y if y>1:
        print("Positive Number Greater Than One")
    case _ if y<-1:
    #case y if y<-1:
        print("Negative Number Less Than Negative One")
    case _:
        print("Unmatched Case")

#Switch case uses to match patterns
numbers = [4,3,5]
match numbers:
    case [x,y]:
        print(x*y)
    case [x,y,z]:
        print(x+y+z)
    case _:
        print("This list doesnot contain 2 or 3 numbers")

x = [1,2,3]
match x:
    case []:
        print("Empty List")
    case [a]:
        print("List has one element")
    case [a,b]:
        print("List has two element")
    case _:
        print("This is something else")