# python oop practice
# python exercise from pynative

class Vehicle:
    color = "White"

    def __init__(self, name, max_speed, mileage, capacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity
        
    def seating_capacity(self):
        return f"The seating capacity of a {self.name} is {self.capacity} passengers"
    
    def fare(self):
        return self.capacity * 100


class Bus(Vehicle):
    def fare(self):
        amount = super().fare()
        amount = amount + (0.1 * amount)
        return amount


class Car(Vehicle):
    pass


bus1 = Bus("School Bus", 180, 12, 50)

print("Vehicle:", bus1.name)
print("Color:", bus1.color, " Speed:", bus1.max_speed, " Mileage:", bus1.mileage)
print("Total bus fare:", bus1.fare())
print(type(bus1))
print(isinstance(bus1, Vehicle))
print("\r")

car1 = Car("Taxi", 220, 20, 5)

print("Vehicle:", car1.name)
print("Color:", car1.color, " Speed:", car1.max_speed, " Mileage:", car1.mileage)
print("Total taxi fare:", car1.fare())