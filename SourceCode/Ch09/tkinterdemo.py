import tkinter as tk
from tkinter import messagebox

def handle_button_click():
    text = textbox.get("1.0", "end-1c")
    messagebox.showinfo("Button Clicked", f"Textbox Value: {text}")

def handle_menu_about():
    messagebox.showinfo("About", "This is a sample Tkinter application.")

window = tk.Tk()
window.title("Tkinter Demo")

# Menu
menu_bar = tk.Menu(window)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Exit", command=window.quit)

help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=handle_menu_about)

menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label="Help", menu=help_menu)

window.config(menu=menu_bar)

# Textbox
textbox = tk.Text(window, height=5, width=30)
textbox.pack(pady=10)  # Add vertical padding

# Button
button = tk.Button(window, text="Click Me", command=handle_button_click)
button.pack(pady=10)  # Add vertical padding

window.mainloop()
