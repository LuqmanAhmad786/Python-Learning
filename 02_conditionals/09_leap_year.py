year = 2023

if (year % 400 == 0) or (year % 4  == 0 and year % 100 != 0):
  print(year," Leap year")
else:
  print(year, " Is not leap year")