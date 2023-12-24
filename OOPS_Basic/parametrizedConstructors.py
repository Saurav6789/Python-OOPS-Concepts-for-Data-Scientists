"""The parameterized constructor has multiple parameters along with the self. Consider the following example.
"""

class Shape :
    def __init__(self,category,dimensions) -> None:
        self.category = category
        self.dimensions = dimensions
        

square = Shape("quadrilateral",2)
print(f"Shape 1: {square.category} {square.dimensions}")
     
        