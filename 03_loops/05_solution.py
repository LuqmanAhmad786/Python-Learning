input_str = "teeteracacd"

for char in input_str:
  print(char)
  if input_str.count(char) == 1:
    print("First Non Repeated Char is: ",char)
    break