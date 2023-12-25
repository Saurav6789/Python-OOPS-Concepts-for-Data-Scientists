# Filename: dunder_methods_example.py

class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"{self.id} of {self.name}"

    def __eq__(self, other):
        if isinstance(other, Employee):
            return self.id == other.id and self.name == other.name
        return False

    def __len__(self):
        return len(self.id)

# Creating instances of the Book class
emp1 = Employee(id="A2345", name="Saurav Anand")
emp2 = Employee(id="A3425", name="Vishal Rathore")

# Using dunder methods
print(Employee)            # Calls __str__
print(len(emp1))       # Calls __len__
print(emp1 == emp2)   # Calls __eq__
