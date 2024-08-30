#This is my python project
import tkinter as tk
root = tk.Tk()
root.title("calculator")

result_label = tk.Label(root, text="", width=20, font=("Arial", 24), borderwidth=2, relief="solid")
result_label.grid(row=0, column=0, columnspan=4)

def update_label(item):
    current_text = result_label.cget("text")
    result_label.config(text=current_text + item)

root.mainloop()