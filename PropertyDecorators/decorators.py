"""In Python, properties, setters, and deleters are used to implement managed attributes in classes. 
These features allow you to control the access, modification, and deletion of attributes in a class.
"""

class Employee:
    def __init__(self) -> None:
        self.__name = ""
    
    #Using property decorator
    @property
    
    #getter method
    def name(self):
        return self.__name
    
    #setter method
    @name.setter
    def name(self,value):
        self.__name = value
    
    
    #Deleter method
    @name.deleter
    def name(self):
        del self.__name
        
#Creating an object
emp1 = Employee()

#Setting the name
emp1.name= "Saurav"

#Prints name 
print(emp1.name)

#Deletes name
del emp1.name

#Prints name of the deleted value
print(emp1.name)

        
    
        