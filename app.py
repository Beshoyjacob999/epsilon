#This is my python project
import tkinter as tk
root = tk.Tk()
root.title("calculator")

result_label = tk.Label(root, text="", width=20, font=("Arial", 24), borderwidth=2, relief="solid")
result_label.grid(row=0, column=0, columnspan=4)

root.mainloop()