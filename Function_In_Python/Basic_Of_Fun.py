#/////////////////////////////////////////// FUNCTION ////////////////////////////////////////////////////////////
# A function is a block of code which only runs when it is called.You can pass data, known as parameters,
# into a function.A function can return data as a result.



def sum_fun(x,y): # funtion declaration
    res=x+y   # funtion defination
    print(res)
sum_fun(4,5) # function call

def division_fun(num1,num2): # num1 and num2 is parametter
    res=num1/num2
    return res
get_result=division_fun(4,2) # 4,2 is Arguments
print(get_result)

def Two_val(x=30,y=20): # We can set default parametter
    add=x+y
    return add
get_val=Two_val()
print(get_val)


def Two_val(x,y): 
    add=x+y
    sub=x-y
    return add, sub # we can return multple value and this value store in tuple.
get_val=Two_val(20,30)
print(get_val, type(get_val))

def get_coordinates():
    return 10, 20
x, y = get_coordinates()
print(x, y)  # Output: 10 20



# IN PYTHON FUNCTION ARE OF TWO TYPE
 # 1. BUITL IN FUNCTION print(), len(), type(), range()......
 # 2. User defined function


# def City_name(city):
#     lenth= len(city)
#     return lenth, city

# city=["Delhi", "Mumbie", "Bhagalpur", "Kolkata"]
# get=City_name(city)
# print(get)
   

def factorial(num):
    for i in range(num):
        facto=num*i
    return facto

get_facto=factorial(5)
print(get_facto)


