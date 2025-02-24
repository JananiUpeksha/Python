class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print(self.name,"Says woof")

class Cat(Animal):
    def __init__(self,name,colour):
        super().__init__(name)
        self.colour = colour 

dog = Dog("Roxy")
dog.speak()
cat = Cat("Kitty","Black")
print(cat.name,cat.colour)


