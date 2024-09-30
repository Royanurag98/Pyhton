# _ _init_ _ Function :
# _ _init_ _ Function is bacilly a constructor
# All classes have a function called  _ _init_ _() (constructor) which is always execute when the object is being created


class Electronic_Product:
# Here we create a contructor if i not create constructor manually it automatic created when objet is created
# The self parameter is a refernce to the current object of the class and is used to access variable that belong to the class
     # Default constructor 
     def __init__(self):
            pass
      # Parameterized constructor : if you use parameterized constructor in taht case we default contructor is not execute.
     def __init__(self, P_name, P_price, P_color, ) : #  Self is by default argument and it refers the object
              self.name=P_name
              self.price=P_price
              self.color=P_color
              print("Now we are creating a constructor manually ")


product1=Electronic_Product("Mobile", 20000, "Red") # Here we create instance(object) of class
print( product1.name, product1.price,product1.color)

product2=Electronic_Product("Laptop", 50000, "Green")
print( product1.name, product1.price,product1.color)

  