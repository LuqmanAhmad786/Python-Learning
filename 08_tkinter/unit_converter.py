import tkinter as tk


window = tk.Tk()
window.title("Unit Converter")

def celsius_to_fahrenheit():
  try:
    celsius = float(celsius_entry.get())
    fahrenheit = (celsius * 9/5) + 32
    result_label.config(text=f"{celsius:.2f}°C = {fahrenheit:.2f}°F")
  except ValueError:
    result_label.config(text="Please enter a number ")

def fahrenheit_to_celsius():
  try:
    fahrenheit = float(fahrenheit_entry.get())
    celsius = (fahrenheit - 32) * 5/9
    result_label.config(text=f"{fahrenheit:.2f}°F = {celsius:.2f}°C")
  except ValueError:
    result_label.config(text=" invalid input")





celsius_label = tk.Label(window, text="Input Celcius: ")
celsius_label.grid(row=0, column=0)

celsius_entry = tk.Entry(window)
celsius_entry.grid(row=0, column=1)

c_to_f_button = tk.Button(window, text="Convert to Foehrenheit", command= celsius_to_fahrenheit)
c_to_f_button.grid(row=0, column=2)

fahrenheit_label = tk.Label(window, text="Fahrenheit: ")
fahrenheit_label.grid(row=1, column=0)

fahrenheit_entry = tk.Entry(window)
fahrenheit_entry.grid(row=1, column=1)

f_to_c_button = tk.Button(window, text="Convert to Celsius", command= fahrenheit_to_celsius)
f_to_c_button.grid(row=1, column=2)

result_label = tk.Label(window, text="", font=("Helvetica", 14))
result_label.grid(row=2, columnspan=3)

window.mainloop()