"""This module is about the construtor used in python. The method the __init__() simulates the constructor of
the class. This method is called when the class is instantiated. It accepts the self-keyword as a first 
argument which allows accessing the attributes or method of the class. 
"""

class Animal:
    def __init__(self,category,sound) -> None:
        self.category = category
        self.sound = sound
        

tommy = Animal("Dog","Bark")
print(f"Animal 1: {tommy.category} {tommy.sound}")