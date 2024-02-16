import tkinter as tk

window = tk.Tk()
window.title("Layout")

label1 = tk.Label(window, text="Python Exercise", padx=10, pady=10)
labe2 = tk.Label(window, text="Java Exercise", padx=10, pady=10)
label3 = tk.Label(window, text="C++ Exercise", padx=10, pady=10)

label1.pack(side="top")
labe2.pack(side="top")
label3.pack(side="top")

window.mainloop()