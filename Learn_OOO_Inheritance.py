# Class - object

class Car:
    def __init__(self, brand, model):        
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

# car1 = Car("Toyota", "Corolla")

# print(car1.brand)
# print(car1.model)
# print(car1.full_name())

class ElectricCar(Car):
   def __init__(self, brand, model, battery_size):       
       super().__init__(brand, model)  # Call the constructor of the parent class (Car)
       self.battery_size = battery_size  

car2 = ElectricCar("Tesla", "Model 3", "75 kWh")
print(car2.brand)
print(car2.model)   
print(car2.battery_size)
print(car2.full_name())