class MyClass:
    def __init__(self, protected_var, private_var):
        self._protected_var = protected_var
        self.__private_var = private_var

    def _protected_method(self):
        print("This is a protected method")

    def __private_method(self):
        print("This is a private method")
    
    # Nested Example class
    class Example:
        def __init__(self):
            self.__data = None  # Private encapsulated data

        def set_value(self, value):
            self.__data = value

        def get_value(self):
            print("Value of data is:", self.__data)


# Usage of MyClass and Example
my_obj = MyClass("test1", "test2")

# Access protected members (not encouraged)
print(my_obj._protected_var)
my_obj._protected_method()

# Working with the nested Example class
example = MyClass.Example()
example.set_value("Hello World")
example.get_value()

CamScannerCamScannerCamScannerCamScannerCamScannerCamScannerCamScannerCamScannerCamScannerCamScannerCamScannerCamScannerCamScannerCamScannerCamScannerCamScannerCamScannerCamScannerCamScannerCamScanner