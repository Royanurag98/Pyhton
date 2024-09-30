#////////////////////////////////////////////// FUNCTION OF STRING ///////////////////////////////////

# 1. LENGTH//////////////////////////////////////
# len() function IS USE TO FIND THE LENGHT OF STRING.
Intro='My name is Anurag Kumar'
print(Intro)
print("Lenght of String is :",len(Intro))

# 2. endsWith() :It returns true if string ends with sub string whatever we pass inside the endswith function as a callback.
str="anurag Roy"
print(str.endswith("Roy"))

# 3. capitalized() : It is use to make the first latter of srings is capital latter.
print(str.capitalize())

# 4. replace() : it is use to replace the latter from string
print(str.replace('g', 'j'))

# 5. find() : It is use to find the index of latter or word from the strings which comes first 
str2="Hellow i am Anurag Roy and i am from bihar" 
print(str2.find("am")) 
# count() : It use to find the count means how may particular word and latter exist in the string
print(str2.count("a"))