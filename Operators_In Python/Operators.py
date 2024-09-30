#///////////////////////////////////// OPERATORS IN PYTHON////////////////////////////////////////

# Python divides the operators in the following groups:

# Arithmetic operators => + , -, *, /, %, **, //
# Assignment operators =>
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators


# ////////////////////////////////////////////// ARITHMETIC OPERATORS //////////////////////////////////////

X=4 
Y=2
print("	Addition	     x + y  = ", X + Y  ) 
print("	Subtraction	     x - y  = ", X - Y  ) 
print(" Multiply         x * y  = ", X * Y  ) 
print("	Division	     x / y  = ", X / Y  ) # It gives the resut in decimal
print("	Modulus	         x % y	= ", X % Y  )   
print("	Exponentiation	 x ** y	= ", X ** Y ) # 4 per power 2
print(" Floor division	 x // y = ", X // Y ) # floor division // rounds the result down to the nearest whole number




# //////////////////////////////////////////////////////// ASSIGNMENT OPERATORS //////////////////////////////////////////
num1=8
num2=3

num3=num2
print("	=	  x = y     x + y   ",  num3 )
num1 += num2  
print("	+=	  x += 3	x = x + 3   ", num1  )
num1 -= num2   
print(" -=	  x -= 3	x = x - 3   ",  num1  )
num1 *= num2  
print("*=	  x *= 3	x = x * 3	",  num1  ) 
num1 /= num2 
print("	/=	  x /= 3	x = x / 3   ",  num1  )
num1 %= num2    
print("	%=	  x %= 3	x = x % 3	",  num1  ) 
num1 //= num2 
print(" //=	  x //= 3	x = x // 3	",  num1 ) 

num1 = 8
num1 &= num2 
print(" &=  x &= 3  x = x & 3   ", num1)  # Output: num1 = 8 & 3 = 0

num1 = 8  # Resetting num1 to its original value
num1 |= num2  
print(" |=  x |= 3  x = x | 3   ", num1)  # Output: num1 = 8 | 3 = 11

num1 = 8  # Resetting num1 to its original value
num1 ^= num2  
print("^=  x ^= 3  x = x ^ 3   ", num1)  # Output: num1 = 8 ^ 3 = 11

num1 = 8  # Resetting num1 to its original value
num1 >>= num2  
print(">>=  x >>= 3  x = x >> 3  ", num1)  # Output: num1 = 8 >> 3 = 1

num1 = 8  # Resetting num1 to its original value
num1 <<= num2 
print("<<=  x <<= 3  x = x << 3  ", num1)  # Output: num1 = 8 << 3 = 64


#///////////////////////////////////////////////// COMPARISION OPERATORS //////////////////////////////////////////
print(" ==	Equal	                     x == y	 ", X == Y) 
print(" >	Greater than	             x > y   ", X > Y) 
print(" <	Less than	                 x < y   ", X < Y) 
print(" >=	Greater than or equal to	 x >= y	 ", X >= Y)
print("	<=	Less than or equal to	     x <= y  ", X <= Y)   
print(" !=	Not equal	                 x != y	 ", X != Y) 

#/////////////////////////////////////////////////// LOGICAL OPERATORS ////////////////////////////////////
print(" and Returns True if both statements are true	    x < 5 and  x < 10	 ", X < 5 and  X < 10) 
print(" or	Returns True if one of the statements is true	x < 5 or x < 4	     ", X < 5 or X < 4) 
print(" not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)", not(X < 5 and X < 10)) 

#//////////////////////////////////////////////////// IDENTITY OPERATORS ////////////////////////////////////
FruitObj1 = ["apple", "banana"]
FruitObj2 = ["apple", "banana"]
FruitObj3 = FruitObj1
print("is 	    Returns True if both variables are the same object	x is y		         ", FruitObj1 is FruitObj2) 
print("is not	Returns True if both variables are not the same object	x is not y	     ", FruitObj2 is FruitObj3) 	


#//////////////////////////////////////////////////// MEMBERSHIP OPERATORS ////////////////////////////////////
print("in 	    Returns True if  specified value is present in the object	x in y	        ", "banana" in FruitObj1) 
print("not in	Returns True if  specified value is not present in the object	x not in y  ", 'mango' is FruitObj1) 	









	
	




	
	

	


