class Car:
  total_cars = 0
  def __init__(self , brand , model):
    self.__brand = brand
    self.__model = model
    Car.total_cars += 1

  def get_brand(self):
    return self.__brand

  def full_name(self):
    return f"{self.__brand} {self.__model}"

  def fuel_type(self):
    return "Petrol or Diesel"

  @staticmethod
  def general_description():
    return "This is an electric car. It does not require petrol or diesel to run. It runs on electric charge."

  @property
  def model(self):
    return self.__model


class ElectricCar(Car):
  def __init__(self,brand , model, battery_size):
    super().__init__(brand, model)
    self.battery_size = battery_size

  def fuel_type(self):
    return "Electric Charge"



# my_tesla = ElectricCar("Tesla", "Model S", 75)

# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, ElectricCar))
# print(my_tesla.brand)
# print(my_tesla.get_brand())
# print(my_tesla.model)
# print(my_tesla.battery_size)
# print(my_tesla.fuel_type())

# safari = Car("Tata", "Safari")
# print(safari.get_brand())
# print(safari.model)
# print(safari.fuel_type())

# honda = Car("Honda", "Civic")
# print(honda.get_brand())
# print(honda.model)
# print(honda.fuel_type())

# print(honda.general_description())
# print(Car.total_cars)

# print(Car.general_description())
# my_car =Car("Toyota", "Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

# my_new_car = Car("Honda", "Civic")
# print(my_new_car.brand)
# print(my_new_car.model)
# print(my_new_car.full_name())

# my_car = Car("Toyota", "Corolla")
# # my_car.model = "Corolla 2021"
# print(my_car.model)
class Battery:
  def battery_info(self):
    return f"The battery size of the car is"
class Engine:
  def engine_info(self):
    return f"The engine of the car"

class ElectricCarTwo(Car , Battery , Engine):
  pass


my_new_tesla = ElectricCarTwo("Tesla", "Model S")
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())
