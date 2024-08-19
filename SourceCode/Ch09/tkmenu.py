from tkinter import *

# Create the main window
window = Tk()

# Set the window title
window.title("Tk")

# Set the initial size and position of the window.
window.geometry("800x600+50+20")

def endit():
    print ('program exiting')

# Menu
menubar = Menu(window)
window.config(menu=menubar)

# Create file menus
filemenu = Menu(menubar, tearoff=0)

# Add items to menu
filemenu.add_command(label="Exit", command=endit)


# Add file menu to menu bar
menubar.add_cascade(label="File", menu=filemenu)


# Start the Tkinter event loop
window.mainloop()
