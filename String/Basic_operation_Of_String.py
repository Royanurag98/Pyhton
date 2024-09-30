#////////////////////////////////////////////// BASIC OPERATION OF STRING ///////////////////////////////////

# 1. STRING CONCATINATE///////////////////////////
firstName="Anurag"
lastName="Kumar"
print( "My name is ",firstName + lastName)
print( "My name is ",firstName + " " + lastName)



# 3. INDEXING//////////////////////////////////////
#  indexing start with 0
#  We can access character through positive indexing as well as negative indexing

str="Anurag Roy"
print(str[1])
print(str[-3])
# here we try to add underscore in vecent place we cant do that because we can not modefy string only access
# str[7]="_" 
# print(str)

# 4. SLICING////////////////////////////////////////
# Slicing is used to access the subset  of string
# string[Starting index : Ending index] ending index is not included
str="MynameisAnurag"
print(str[ 2 : 5 ])# start from index 2 and excluding index 5
print(str[ 2 : len(str)  ])
print(str[   : 5 ])# str[0:5] 
print(str[ 2 :   ]) #str[2:len(str)]

print("Negative slicing")
print(str[ 2 : -7])
print(str[ -5 : -2])