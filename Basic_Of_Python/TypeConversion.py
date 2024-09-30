#////////////////////////////////////////// TYPE CONVERSION IN PYTHON /////////////////////////////////////////////////

# TYPE CONVERSION ARE OF TWO TYPE 
#1. IMPLICIT TYPE CONVERSION :
     # Implicit Type Conversion is also known as ‘automatic type conversion‘. It is done by the compiler on its own

num1=4
num2=2.5
print(num1+num2)# Return 6.5 because compiler auto convert interger to float because float priority is high compaire to int

num3=3
print(num1+num3) # Return 7 only not in float

#2. EXPLICIT TYPE CONVERSION :
     # Explicit type conversion is also known as ‘Type Casting‘. it is done by the user by using (type) operator.

A=2
B=3.7
X=int(B)
print(A+X)