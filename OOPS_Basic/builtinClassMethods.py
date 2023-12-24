"""There are certain built in class methods which are defined in the below example 
    """
    
class Employee :
    def __init__(self, name, id, age) -> None:
        self.name = name
        self.id =id
        self.age = age
            
#Create an object for the class object 

emp1 = Employee("Saurav",1231,35)

#prints the attribute name of the object emp1
print(getattr(emp1, 'name'))    

# reset the value of attribute age to 23  
setattr(emp1, "age", 36)

# prints the modified value of age  
print(getattr(emp1, 'age')) 

# prints true if the student contains the attribute with name id  
  
print(hasattr(emp1, 'id'))  

# deletes the attribute age  
delattr(emp1, 'age') 

# this will give an error since the attribute age has been deleted  
print(emp1.age)  