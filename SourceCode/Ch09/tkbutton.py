from tkinter import *

# Create the main window
window = Tk()

# Set the window title
window.title("Tk")

# Set the initial size and position of the window.
window.geometry("800x600+50+20")

def endit():
    print('program exiting')

myButton = Button(window, text="End", command=endit)  # Use command=endit to associate the function with the button

myButton.pack()
myButton.place(x=100, y=100)

# Start the Tkinter event loop
window.mainloop()
