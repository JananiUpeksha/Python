file1 = open("myfile.txt")
file_content = file1.read()
#file_content = file1.readline() 1st line eka withri run wenne
print(file_content)
file1.close()
"""
file1 = open("myfile.txt")
file_content = file1.readlines()
print(file_content,type(file_content))
"""

#file eka close krnna one na mehema liuwama
with open("myfile.txt","r") as file2:
    content = file2.read()
    print(content)

"""
file3 = open("myfile1.txt", "w")
file3.write("Hello world\n")
file3.write("This is our Python class\n")
file3.close()
"""
"""
with open("myfile1.txt", "w") as file3:
    file3.write("Hello world\n")
    file3.write("This is IJSE\n")
"""

with open("myfile1.txt", "w") as file3:
    file_data = ["Hello world.\n", "This is IJSE.\n"]
    file3.writelines(file_data)
print(file_data)

with open("myfile1.txt", "a") as file3:
    file3.write("We are globle citizen")
with open("myfile1.txt", "r") as file3:
    content1 = file3.read()
print(content1)

"""
Implement simple contact mng system
- create a programme that stores and manage contat in a file name contact.txt each contact should include name, phone num and email
- features to implemet 
    - add a new contact - append a contact to a file 
    - view all contact - read and display all contact from the file
    - exit the programe
"""