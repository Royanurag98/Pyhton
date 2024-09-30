#///////////////////////////////////////////////// TUPLE ///////////////////////////////////////////
# A Tuple is a built in data type that allows you to store multiple type of items
# in a single variable and this item can be different data type.
# Tuples are immutable, meaning once you create a tuple, you cannot change, add, or remove its elements.
# Tupple items store inside the () (parenthasis)


# Creating a tuple of number
tup=(1,2,3,4,5,"Anurag", True)
print(tup, type(tup))
# We can create empty tupple
tup2=()
print(tup2, type(tup2))

# if you store  single item in tupple the right way to store is tup3(2,)  other wise it treated as a normal data type
tup3=(2,) # This is treated like tuple data type
print(tup3, type(tup3)) 
tup4=(2)  # This is treated like int data type
print(tup4, type(tup4))

fruits=("apple", "banana", "cherry","mango")
# Accessing items in a tuple through index
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana

# Slicing is also allowed in tuple
print(fruits[1:3])



# #  SOME OF THE TUPLE PREDEFINED FUNCTION/////////////////////////////////////////////
# 1. index(element) : It return the index number of first occurrence of that elemnt
tup6=[1,4,2,6,3,6,8,6]
print(tup6.index(6))

# 2. count(element) : It return the count of total occurrences of element
print(tup6.count(6))

