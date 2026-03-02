
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def fuel_type(self):
        return "Gasoline"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)  # Call the constructor of the parent class (Car)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric"
    
car1 = Car("Toyota", "Corolla")
car2 = ElectricCar("Tesla", "Model 3", "75 kWh")

print(car1.fuel_type())  # Output: Gasoline
print(car2.fuel_type())  # Output: Electric
# same method name - but different implementation in parent and child class - 
# this is polymorphism.
