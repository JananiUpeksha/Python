#lambda arguments: expression
#lambda - keyword that indicate the creation of lamda function
#argument - input para for function similar to regular function
#expression - the single expression that lambda function will evaluate and return

add = lambda x,y:x+y
print(add(3,9))
#without assigning to variable
add = (lambda x,y:x+y)(5,5)
print(add)

#write programme that:
#take a list of tuples,where each tuple contain a name(string) and age(int).
#use a lambda function to filter out the tuple where the age is less than 18
#print the list of tuples after filtering
people=[("aaa",22),("bbb",14),("ccc",34),("ddd",15)]
filter_list = filter(lambda x:x[1]>=18 , people)#filter method eka use krnna pluwn iterate krnna 
filter_list = list(filter_list)
print(filter_list)

#Arbitrary keyword arguments(**kwargs) - dictonary ekak krla ewanne
def arbitrary_keywords_args(**kwargs):
    print(kwargs,type(kwargs))
    for key,value in kwargs.items():
        print("key = ", key , "value = ",value)
arbitrary_keywords_args(name="senu",age=23,city="panadura")


#use the same fun definition to make function that always double the number you send in
def myfunc(n):
    return lambda a:a*n

my_doubler = myfunc(2) #my_doubler -> lambda a:a*2
print(my_doubler(5))

#decide the maximum num between 2 numbers
find_max = lambda x,y: x if x>y else y
print(find_max(13,99))



