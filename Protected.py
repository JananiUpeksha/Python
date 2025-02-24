class Animal:
    def __init__(self,name):
        self.name = name

    def _make_sound(self):
        print("some sounds")

class Dog(Animal):
    def bark(self):
        self._make_sound()
        print(self.name,"is barking")

dog = Dog("Roxy")
dog.bark()

"""
implemet a quadartric equalation class that reprenset a quadartric equalation of the form ax2+bx+c the class should have 
attribute - private attributes __a,__b and __c to store the core officient of the quadartric equalation
methods - a constructor to initialize the core officernt __a,__b and __c
        - a private method __descriminent that calculate and retuen the __descriminent(D = b2-4ac)
        - a public method find_routes that use the private __descriminent method 
        - return the root of the quadartric equalation 
            - if D=0 one real root
            - if D>0 to distinct real roots
            - id D<0 2 complex roots
"""

class QuadartricEqualation:
    def __init__(self,a,b,c):
        self.__a = a
        self.__b = b
        self.__c = c

    def __descriminent(self):
        return self.__b**2 -4 * self.__a * self.__c

    def find_roots(self):
        D = self.__descriminent()
        if D>0:
            root_1 = (_self.__b+D)