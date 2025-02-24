class Car:
    category = "motor vehicle"

    def __init__(self, model, colour):
        self.model = model
        self.colour = colour

    def display(self):
        print("This is a display function")

    def display_attributes(self):
        print(self.model)
        print(self.colour)

    def update(self,new_model,new_colour):
        self.model = new_model
        self.colour = new_colour



# Creating an instance of Car with no attributes (default category usage)
new_car = Car("Default Model", "Default Colour")  # Providing default values
print(new_car.category)
new_car.display()

# Creating an instance of Car with specific attributes
new_car1 = Car("Audi", "Black")
new_car1.display_attributes()


new_car1.update("Audi", "Black")
new_car1.display_attributes()
print(Car.category)

#create a class name bank account an attrubute account_holder to store account holder and attribut balance to store the account balance initalize to 0 add following methos to class
#deposit - add given ammount to the balance
#widrow - subsract the given amount from the balance if sufficient fund exsist otherwise print an error msg
#display balane