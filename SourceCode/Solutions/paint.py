import tkinter as tk

def start_drawing(event):
    global last_x, last_y
    last_x = event.x
    last_y = event.y

def draw(event):
    global last_x, last_y
    canvas.create_line(last_x, last_y, event.x, event.y, fill=current_color.get(), width=pen_size.get())
    last_x = event.x
    last_y = event.y

def change_color():
    color = color_var.get()
    current_color.set(color)

def change_pen_size():
    size = int(size_var.get())
    pen_size.set(size)

# Create the main window
window = tk.Tk()
window.title("Simple Paint Program")

# Create a canvas for drawing
canvas = tk.Canvas(window, width=400, height=400)
canvas.grid(row=0, column=0, columnspan=2)

# Bind mouse events to canvas
canvas.bind("<Button-1>", start_drawing)
canvas.bind("<B1-Motion>", draw)

# Create a color selection menu
color_var = tk.StringVar()
color_var.set("black")
color_menu = tk.OptionMenu(window, color_var, "black", "red", "green", "blue")
color_menu.grid(row=1, column=0, sticky="nsew")

# Create a button to change the line color
change_color_btn = tk.Button(window, text="Change Color", command=change_color)
change_color_btn.grid(row=1, column=1, sticky="nsew")

# Variable to store the current line color
current_color = tk.StringVar()
current_color.set("black")

# Variable to store the line thickness
pen_size = tk.IntVar()
pen_size.set(1)

# Create a pen size selection menu
size_var = tk.StringVar()
size_var.set("1")
size_menu = tk.OptionMenu(window, size_var, "1", "2", "3", "4", "5")
size_menu.grid(row=2, column=0, sticky="nsew")

# Create a button to change the pen size
change_size_btn = tk.Button(window, text="Change Size", command=change_pen_size)
change_size_btn.grid(row=2, column=1, sticky="nsew")

# Center the buttons and menus in their cells
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)

# Start the Tkinter event loop
window.mainloop()
