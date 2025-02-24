"""def add():
    with open("myfile1contact.txt", "a") as file:
        name = input("Name: ")
        number = input("Contact number: ")
        mail = input("E-mail: ")
        temp = name + " " + number + " " + mail + "\n"
        file.write(temp)

def view():
    with open("myfile1contact.txt", "r") as file:
        contacts = file.readlines()
        for contact in contacts:
            print(contact.strip()) 

while True:
    print("\nEnter 1 to add the contact ")
    print("Enter 2 to view the contacts ")
    print("Enter 3 to exit ")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add()
    elif choice == "2":
        view()
    elif choice == "3":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
"""
def add(contact_count):
    with open("myfile1contact.txt", "a") as file:
        name = input("Name: ")
        number = input("Contact number: ")
        mail = input("E-mail: ")
        temp = name + " " + number + " " + mail + "\n"
        file.write(temp)
    contact_count += 1
    return contact_count

def view():
    with open("myfile1contact.txt", "r") as file:
        contacts = file.readlines()
        for contact in contacts:
            print(contact.strip()) 

# Initialize the contact counter
contact_count = 0

while True:
    print("\nEnter 1 to add the contact ")
    print("Enter 2 to view the contacts ")
    print("Enter 3 to exit ")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        if contact_count < 3:
            contact_count = add(contact_count)
        else:
            print("You have already added 3 contacts. Exiting now.")
            break
    elif choice == "2":
        view()
    elif choice == "3":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
