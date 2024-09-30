#///////////////////////////////////////////////// LIST ///////////////////////////////////////////
# A list is a built in data type that allows you to store multiple type of items
# in a single variable and this item can be different data type.
# list is  Mutable(You can change, add, or remove items from a list).
# list items put inside the  [] (Square brackets)

# List items are stored in a specific order, and each item has an index that starts at 0.
#Creating a list of fruits
fruits = ["apple", "banana", "cherry","mango"]
print(fruits, type(fruits))
# We can create empty tupple
tup2=[]
print(tup2, type(tup2))

# Accessing items in a list through index
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana

# Slicing is also allowed
print(fruits[1:3])

# LIST IS ALSO  MUTABLE (You can change, add, or remove items from a list).

# Update an item in the list
fruits[1] = "grape"
print(fruits)  # Output: ['apple', 'grape', 'orange']

# #  SOME OF THE LIST PREDEFINED FUNCTION/////////////////////////////////////////////

# 1. append() :it is use to add the item from last in existing list and we can add similar type of data.
number=[2,5,8,4,9,6,1]
number.append(20) # [2, 5, 8, 4, 9, 6, 1, 20]
print(number)

# 2. sort() : it is use to short the list items in accending order
print(number.sort())# it print none value because sort method not return anything
print(number) 

# 3. sort(reverse=True) : It is use to short the list items in decending order 
number.sort(reverse=True)
print(number) 

# 4. reverse() :It is uset reversed the  list
number.reverse()
print(number) 

# 5. insert(index, item) : it is use to insert the value in particular place in list. and list is grow not
                      # remove thet list item where we insert the item
number.insert(3,35)
print(number) 

# 6. remove() : it use to remove the item from list which is first occurrence
number.remove(5)
print(number)

# 7. pop(): it use remove the items at any index.
number.pop(3)
print(number)

