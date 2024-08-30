#This is my python project
import tkinter as tk
root = tk.Tk()
root.title("calculator")

result_label = tk.Label(root, text="", width=20, font=("Arial", 24), borderwidth=2, relief="solid")
result_label.grid(row=0, column=0, columnspan=4)

def update_label(item):
    current_text = result_label.cget("text")
    result_label.config(text=current_text + item)

def calculate():
    try:
        result = str(eval(result_label.cget("text")))
        result_label.config(text=result)
    except:
        result_label.config(text="خطأ")

def clear():
    result_label.config(text="")

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 1
col = 0

root.mainloop()