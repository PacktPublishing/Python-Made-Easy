import tkinter as tk

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

window = tk.Tk()
window.title("Calculator")

entry = tk.Entry(window, width=30)
entry.grid(row=0, column=0, columnspan=4)


buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

for btn_text, row, col in buttons:
    button = tk.Button(window, text=btn_text, width=5, command=lambda text=btn_text: entry.insert(tk.END, text))
    button.grid(row=row, column=col)

clear_button = tk.Button(window, text="C", width=5, command=lambda: entry.delete(0, tk.END))
clear_button.grid(row=4, column=2)

equal_button = tk.Button(window, text="=", width=5, command=calculate)
equal_button.grid(row=4, column=3)



window.mainloop()
