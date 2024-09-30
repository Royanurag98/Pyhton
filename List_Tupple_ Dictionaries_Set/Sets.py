#///////////////////////////////////////////////// SETS ///////////////////////////////////////////
# A Set is a built in data type that allows you to store multiple type of items but all item will be unique.
# Set is mutable, meaning once you create a set, you can  change, add, or remove its elements 
# But element of set are  immutable set never allow you to add immutable value so we can not add list and disctonary 
# Set items store inside the {} (curlibrases)


#Creating a list of fruits
set1={2,3,4,"Anurag","Kumar", 5,3,4,"Anurag"} # set ignore the duplicate value
print(set1, type(set1))
# We can create empty set
# Creating an empty set (note: {} creates an empty dictionary, not a set)
empty_set = set()
print(empty_set)


my_set = {1, 2, 3}
my_list = [4, 5, 6]

# Attempt to add a list (mutable) to a set
my_set.add(my_list)  # This will raise an error: TypeError: unhashable type: 'list'

my_set = {1, 2, 3}
my_tuple = (4, 5, 6)

# Add a tuple (immutable) to a set
my_set.add(my_tuple)
print(my_set)  # Output: {1, 2, 3, (4, 5, 6)}


# Creating a set
fruits = {"apple", "banana", "cherry"}

# Adding a new element
fruits.add("orange")
print(fruits)  # Output might be: {'orange', 'banana', 'apple', 'cherry'}

# Removing an element
fruits.remove("banana")
print(fruits)  # Output might be: {'orange', 'apple', 'cherry'}
# Clear element form set
fruits.clear()
print(fruits)  

# pop() get the random value form set
fruits.pop()
print(fruits)  
# Performing set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union
print(set1 | set2)  # Output: {1, 2, 3, 4, 5}

# Intersection
print(set1 & set2)  # Output: {3}

# Difference
print(set1 - set2)  # Output: {1, 2}

# Symmetric Difference
print(set1 ^ set2)  # Output: {1, 2, 4, 5}