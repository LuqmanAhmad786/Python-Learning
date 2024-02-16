import tkinter as tk
from tkinter import messagebox

def validate_login():
  userid = username_entry.get()
  password = password_entry.get()

  if userid == "admin" and password == "password":
    messagebox.showinfo("Login Successfully", "Welcome Admin")
  else:
    messagebox.showerror("Login Failed", "Invalid Username or Password")


window = tk.Tk()
window.title('Login Form')
window.geometry('300x200')

username_label = tk.Label(window, text='Username')
username_label.pack()

username_entry = tk.Entry(window)
username_entry.pack()

password_label = tk.Label(window, text='Password')
password_label.pack()

password_entry = tk.Entry(window, show='*')
password_entry.pack()

login_button = tk.Button(window, text='Login', command = validate_login)
login_button.pack()

window.mainloop()