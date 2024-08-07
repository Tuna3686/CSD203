class Student:
    def __init__(self, name, age):
        self.Name = name
        self.Age = age
    #end def
    def __repr__(self):
        return f"({self.Name}, {self.Age})"
       
