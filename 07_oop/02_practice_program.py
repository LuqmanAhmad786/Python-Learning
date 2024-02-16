class Vehicle:
    color = "White"
    def __init__(self, name,mileage,capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    # def seating_capacity(self, capacity):
    #     return f"The seating capacity of a {self.name} is {capacity} passengers"

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    # assign default value to capacity
    # def seating_capacity(self, capacity=50):
    #     return super().seating_capacity(capacity=50)

    def fare(self):
        amount = super().fare()
        amount += amount * 10 / 100
        return amount


School_bus = Bus("School Volvo", 12, 50)
# print(School_bus.seating_capacity())
# print(School_bus.color)
print ("Total Bus fare is:", School_bus.fare())