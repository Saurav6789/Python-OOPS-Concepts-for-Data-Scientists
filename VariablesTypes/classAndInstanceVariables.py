"""The main two types of variables in python are class and Instance variables. 
Class variables are shared among all instances of a class, while instance variables are unique to each instance.
"""

class Employee:
    
    #Class variables 
    organization = "Intel"
    
    def __init__(self,name,salary) -> None:
        #instance variables 
        self.name = name 
        self.salary =salary
        
    def display_details(self):
        print(f"Employee: {self.name}")
        print(f"Employee ID: {self.salary}")
        print(f"Company: {Employee.organization}")  # Accessing the class variable


# Creating instances of Employee class
employee1 = Employee(name="Saurav", salary=12000)
employee2 = Employee(name="Bob", salary=14000)

# Accessing instance variables and class variable
employee1.display_details()
print("\n")  # Adding a separator for better readability
employee2.display_details()