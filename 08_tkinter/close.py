import tkinter as tk

def close_window():
  window.destroy()

window = tk.Tk()
window.title("Close Window Example")

label = tk.Label(window, text="Close the window to end the program.")
label.pack(padx=25 , pady=25)

close_button = tk.Button(window, text="Close", command=close_window)
close_button.pack()

window.mainloop()