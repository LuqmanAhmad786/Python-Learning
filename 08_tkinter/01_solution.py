import tkinter as tk
from tkinter import Menu
from tkinter import messagebox

window = tk.Tk()
window.title("My First GUI Program")
window.geometry("600x400")
window.configure(background="lightblue")

def show_message():
  messagebox.showinfo("Information", "You clicked the button!")

# Create a menu
menu = Menu(window)
window.config(menu=menu)

file_menu = Menu(menu, tearoff=False)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)

edit_menu = Menu(menu, tearoff=False)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")


help_menu = Menu(menu, tearoff=False)
menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About")

label = tk.Label(window, text="Custom Label", font=("Arial Bold", 18),fg="white", bg="red")
label.pack(pady=10)

button_with_color = tk.Button(window, text="Click me!", font=("Helvetica",14), bg="blue", fg="white")
button_with_color.pack(pady=10)

# Create a button
button = tk.Button(window, text="Click me!", command=show_message)
button.pack()



window.mainloop()