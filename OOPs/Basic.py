#////////////////////////////////////////////////// OOPS //////////////////////////////////////////////////////////
# when start the programming that time follow the Procedural Programming method 
# in Procedural Programming method we have to write repeated code again and again
# Algol, BCPL, C these languages follow the Procedural Programming method.
# over come the Procedural Programming method we use functional programming it increase the reuseblity 
# and then we use object oriented programming it also increase the reuseblity 



# Object-Oriented Programming (OOP) is a programming paradigm that uses objects and classes 
# to structure software in a way that is modular, reusable, and easy to maintain. Python,
# being an object-oriented language, supports OOP concepts like classes, objects, inheritance,
# encapsulation, polymorphism, and more


# CLASS ///////////////////////////////////////////////////////////////////////////////////////////
# Class: Class is A blueprint for creating objects. It defines a set of data and functions
# Object: An instance of a class. When a class is defined, no memory is allocated until an object
#         of that class is created..


# Creating Class
class Cars:
    Color="Red",
    Speed="200KM",
    Avarage="10Km"

# Creating Object(instance of class)
car1 = Cars() # when i create car1 object automatic excute a constructer i.e  _ _init_ _ function
print(car1.Color , type(car1))


