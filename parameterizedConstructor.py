class Addition:
    first = 0
    second = 0
    answer = 0
    
    #parameterized constructor
    def __init__(self,f,s):
        self.first = f
        self.second = s
        #self.answer = answer
        
    #printing data members
    
    def print_num(self):
        print('first number: '+ str(self.first))
        print('second number: '+ str(self.second))
        print('answer is :'+ str(self.answer))
        
    #function that will give the Addition logic
    
    def calculate(self):
        self.answer = self.first + self.second
        
    
#creating an object

obj = Addition(100,200)

#now call the function
obj.calculate()

obj.print_num()