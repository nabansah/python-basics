import math
########################### tuple 1
print ('################################# tuple 1')

def circle_cal1(r):
    area = math.pi * r ** 2
    circum = 2 * math.pi * r   

   
    y = (area,circum) #returning more than one value in a tuple
    return y

a, c = circle_cal1(3)

#'tuple' object is not callable and thus you have to assign to a object and thrn access invidually ,
# unlike list you cannot call directly in print
print(circle_cal1(3)[0])
print(circle_cal1(3)[1])
print(a)
print(c)

print ('################################# tuple 2')

############################### tuple 2
def circle_cal1(r):
    area = math.pi * r ** 2
    circum = 2 * math.pi * r   

   
    #y = (area,circum)  #returning more than one value in a tuple
    return (area,circum)

a, c = circle_cal1(3)

print(circle_cal1(3)[0])
print(circle_cal1(3)[1])
print(a)
print(c)

print ('################################# list 1')

############################### list 1

def circle_cal2(r):
    area = math.pi * r ** 2
    circum = 2 * math.pi * r

    x = [area,circum] #returning more than one value in a list
    return x
 
print(circle_cal2(3)[0])
print(circle_cal2(3)[1])

print ('################################# list 2')

############################### list 2

def circle_cal2(r):
    area = math.pi * r ** 2
    circum = 2 * math.pi * r

    #x = [area,circum] #returning more than one value in a list
    return [area,circum]
 
print(circle_cal2(3)[0])
print(circle_cal2(3)[1])


print ('################################# list 3')

############################### list 3

def circle_cal2(r):
    area = math.pi * r ** 2
    circum = 2 * math.pi * r

    #x = [area,circum] #returning more than one value in a list
    return [area,circum]
 
[a, c] = circle_cal2(3)

print(a)
print(c)

####################### 

#'tuple' object is not callable and thus you have to assign to a object and thrn access invidually ,
# unlike list you cannot call directly in print

t = (10, 20)
#t()          # TypeError: 'tuple' object is not callable
print(t[0])  # 10
a, b = t     # a=10, b=20