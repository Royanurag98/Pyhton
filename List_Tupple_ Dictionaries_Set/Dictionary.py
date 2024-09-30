#///////////////////////////////////////////////// DICTIONARY ///////////////////////////////////////////
# A Dictionary is a built in data type that allows you to store multiple type of data type item in a key:value pair
# We can also store list and  tupple as a value
# We can make a key of int, string, float, bull, tupple but we can not make a key of list because it is mutable data type

# Dictionary is  Mutable(You can change, add, or remove items from a list) , Unorder and not allow duplicate key
# Dictionary items put inside the  {} (Curlly brackets)

#Creating a Dictionary of fruits
# tup2=[]
# print(tup2, type(tup2))
# studentInfo={
#     "First_Name":"Anurag Roy", # String
#      "Subject":["HTML", "CSS", "JavaScript"], #list
#      "Topic":("dictionary","Set"), # tuple
#      "Age":24, #int
#      "Height":5.78 # float
# }
# print(studentInfo, type(studentInfo))


# # Accessing items in a Dictionary through key 
# print(studentInfo["First_Name"]) 

# # DICTIONARY IS ALSO  MUTABLE (You can change, add, or remove items from a list).

# # Update an item in the Dictionary
# studentInfo["First_Name"] = "Anurag"
# print(studentInfo)
# # Set an new item with key:value pair in the Dictionary
# studentInfo["Last_Name"]="Roy"
# print(studentInfo)

# # We can create empty Dictionary
# Dist={}
# print(Dist, type(Dist))


# We can do nesting of  Dictionary

Student={
    "Name":"Anurag roy",
    "Age" : 24,
    "Subject" :{
        "CAP776":"HTML",
        "CAP778":"CSS",
        "CAP779":"JavaScript",
       
    }
}
print(Student["Subject"]["CAP776"])

# #  SOME OF THE DICTIONARY PREDEFINED FUNCTION/////////////////////////////////////////////

# 1. key() : Return all the key of dictionary
print(list(Student.keys()))
# 1. value() : Return all the value of dictionary
print(list(Student.values()))
# 1. items() : Return all the key:valuee pairs of dictionary inside a tuple
print(list(Student.items()))
# 1. get() : Return  the vale of key whatever you pass as callback inside get method 
print(Student.get("Age")) 
# Both the way to access the value of key but
#  if i use get() method in that case if i try to access the valu which is not exist in dictionary int tha case it reeturn none
#  but with the dictonary name in that case give error 
print(Student.get("total")) # none
# print(Student["tota"]) # Error


