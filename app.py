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

for button in buttons:
    if button == '=':
        tk.Button(root, text=button, width=5, height=2, command=calculate).grid(row=row, column=col)
    elif button == 'C':
        tk.Button(root, text=button, width=5, height=2, command=clear).grid(row=row, column=col)
    else:
        tk.Button(root, text=button, width=5, height=2, command=lambda b=button: update_label(b)).grid(row=row, column=col)
    
    col += 1
    if col > 3:
        col = 0
        row += 1

tk.Button(root, text='C', width=5, height=2, command=clear).grid(row=row, column=col)

root.mainloop()