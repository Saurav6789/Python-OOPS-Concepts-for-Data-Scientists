"""In Python, metaclasses are classes for classes. They define how classes behave, allowing you 
to customize class creation. The most common use case for metaclasses is to modify or enhance the behavior 
of class creation. 
"""

# Define a metaclass
class Meta(type):
    def __new__(cls, name, bases, dct):
        # Modify or enhance the class creation process
        dct["version"] = 1.0
        return super().__new__(cls, name, bases, dct)

# Use the metaclass to create a class
class MyClass(metaclass=Meta):
    def display_version(self):
        print(f"Version: {self.version}")

# Creating an instance of MyClass
my_instance = MyClass()

# Accessing the version attribute added by the metaclass
print(f"Class version: {MyClass.version}")

# Calling a method of the instance
my_instance.display_version()


## The above code is from openAI chatGPT 