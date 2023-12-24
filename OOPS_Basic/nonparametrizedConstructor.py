"""The non-parameterized constructor uses when we do not want to manipulate the value or the constructor 
that has only self as an argument.
"""

class Employee:
    def __init__(self) -> None:
        print("This is an example of non parametrized construtor")
    
    def display_message(self):
        print("Hello from employee")
        

#Creating the instance of the class 
emp1 = Employee()
emp1.display_message()