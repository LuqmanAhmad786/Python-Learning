import math
def circle_area(radius):
  area = math.pi * radius ** 2
  circumference = 2 * math.pi * radius
  return area, circumference

a , c = circle_area(10)
print("Area of circle is", a, "and circumference is", c)

