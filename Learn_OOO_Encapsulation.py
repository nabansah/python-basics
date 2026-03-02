# Class - object

class Car:
    def __init__(self, brand, model):        
        self.__brand = brand
        self.__model = model

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
car1 = Car("Toyota", "Corolla")

# print(car1.__brand) # you cannot access the private attribute(prop) directly just creating 
# the object of the class. You have to go through a method to access the private prop - in that
# method you might need to go though auth layer/validation b efore accessing the value - 
# this is encapsulation.

# print(car1.__model)

print(car1.full_name())

