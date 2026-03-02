import math

print ('################################# basic function')

def add(a,b):
   #S print(a+b)
    return (a+b)

print(add(1,2))

print ('################################# optional parameter')
################ optional parameter

def greet(x="piu"):
    return ("Hello " + x)

print( greet('vaishnavi') )

print ('################################# lambda function')
################## lambda function

add = lambda a,b : a+b

print(add(1,2))

print ('################################# variable number of args')
###################### variable number of args
def add(*args):
    print(args) #args is a tuple
    print(*args) #unpacking the tuple to get individual values
    print(len(args)) #length of args

    sum = 0
    for i in args:
        sum += i
    return sum

print(add(1,2,3))
print(add(1,2))

print ('################################# variable number of args in key-value pair')
###################### variable number of args in key-value pair
def greet(**kwargs):
    print(kwargs) #kwargs is a dict
    #print(**kwargs) #unpacking the dict to get individual key-value pairs
    print(len(kwargs)) #length of kwargs

    for key, value in kwargs.items():
        print(key, value)
        print(f"{key} : {value}")

print(greet(name="vaishnavi", age=1)) # print returned none as there is no return statement in the function
greet(name="vaishnavi", age=1, hobby="coding")

###################### yield

#return is used to return a value from a function and exit the function. 

#yield is used to return a value from a generator function and pause the function. 
#The next time the generator function is called, it will resume from where it left off.