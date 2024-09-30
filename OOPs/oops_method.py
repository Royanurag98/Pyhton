# oops has four mail pilers  
# Abstraction :Abstraction means hiding the implementation  details of class and showing only the necessary 
# features to the user.  It can be achieved using abstract classes

class Car:
    def __init__(self) :
        self.accelator= False
        self.brk=False
        self.clutch= False
    
    def Statr(self):
       # Hide the Implementation details
       self.accelator= True
       self.clutch= True
       print("Now Car is Start........................")

car1=Car()
car1.Statr()


# Encapsulation: Encapsulation bundles data and methods into a single unit
# inheritance
# Polymorphism