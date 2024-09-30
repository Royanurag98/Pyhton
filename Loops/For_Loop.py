
# The for loop in Python is used to iterate over a sequence (like a list, tuple, dictionary, set, or string)
# and execute a block of code for each item in the sequence

# Iterating Over a List
# fruits = ["apple", "banana", "cherry"]

# for fruit in fruits:
#     print(fruit)

# # Iterating Over a string
# str="Anurag Roy"

# for latter in str:
#     print(latter)

# # Iterating Over a Dictionary
# person = {"name": "Anurag", "age": 25, "city": "Bihar"}
# # Iterating over keys
# for key in person:
#     print(key)

# # Iterating over values
# for value in person.values():
#     print(value)

# # Iterating over key-value pairs
# for key, value in person.items():
#     print(key, value)




# range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default).
# and stope befoure a specified number.
# range(start, stop, step) syntex
# for value in range(5):
#     print("Print the value less then Range", value)
# for value in range(2,5):
#     print("Print the value less then Range", value)
# for value in range(2,20,3):
#     print("Print the value less then Range", value)

# print the odd number
for odd in range(1,20,2):
    print(odd)

# print the even number
for even in range(2,20,2):
    print(even)

# pass : suppose you create a for loop but you dont want to do any thing right now in that cas we can not leve empty for 
# loop otherwise it gives an error . in that case we use pass keyword as a place holder. we do with condition also like i

print("Our code is start executing .................")
for val in range(5):
   # i want use this loop when we needed so we cant do that directaly so use pass keyword
   pass
print("hello")
print("good morning")


