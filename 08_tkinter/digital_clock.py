import tkinter as tk
import time

window = tk.Tk()
window.title("Digital Clock")

def update_time():
  current_time = time.strftime('%H:%M:%S %p')
  clock_label.config(text=current_time)
  clock_label.after(1000, update_time)

clock_label = tk.Label(window, text="", font=("Helvetica", 48))
clock_label.pack(padx=20, pady=20)

update_time()

window.mainloop()