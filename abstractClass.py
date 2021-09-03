from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def printShape(self):
        return 0     #this work as a based and this thrown an rule on the child class that it should have a print classmethod
    
class rectangle(shape):
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length =7
        self.breadth =8
        
    def printShape(self):
        return self.length*self.breadth
        
obj = rectangle()
print(obj.printShape())
    
    