import math

class Circle:
  def __init__(self, radius):
    self.radius = radius

  def area(self):
    return math.pi * self.radius **2

  def perimeter(self):
    return 2 * math.pi * self.radius

radius =10

result = Circle(radius)
area = result.area()
perimeter = result.perimeter()
print("Area of the circle:", area)
print("Perimeter of the circle:", perimeter)