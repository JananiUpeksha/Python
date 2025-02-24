dict_1 = {"name":"sugar","price":150,"weight":"1kg"}
dict_1 = {
    "name":"sugar",
    "price":150,
    "weight":"1kg"
}
print(dict_1,type(dict_1))
print(len(dict_1))
print(dict_1["weight"]) #change
dict_1["price"] = 300.50
dict_1.update({"name":"biscuts","price":250,"weight":"3.5kg"}) #update
print(dict_1)
dict_1["coloue"] = "white" #add
print(dict_1,len(dict_1))
dict_1.pop("weight") #delete
print(dict_1,len(dict_1))

dict_2 = {
    "name":"sugar",
    "price":150,
    "weight":"1kg",
    "name":"floar", #replaced
    "types":{"aaaaa":111,"bbbb":222,"cccc":3333}, #another dict can be in the inside of the dictionary
    "size":"medium"
}
print(dict_2,type(dict_2)) 
dict_2.popitem() #last value will be removed
print(dict_2) 
del dict_2["weight"] #delete
print(dict_2) 
del dict_2 #whole dict will be deleted

dict_3 = {
    "name":"rice",
    "price":120,
    "weight":"1.5kg",
    
}
dict_4 = dict_3.copy() #copy dict to another dict copy method
dict_4["price"] = 990.50
dict_4 = dict(dict_3) #copy dict to another dict using dict constructor
print(dict_3)
print(dict_4)
print(dict_4.keys())

#Merge dict
dict_1 = {"a":1}
dict_2 = {"b":2}
dict_3 = dict_1|dict_2
print(dict_3)

#Get the value
my_dict = {"a":10,"b":20,"c":30}
#my_dict.get(key,default_value)
print(my_dict.get("b"))
print(my_dict.get("d","Not Found"))
