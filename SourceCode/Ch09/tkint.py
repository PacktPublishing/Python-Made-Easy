import tkinter as tk

# Create the main window
window = tk.Tk()

# Set the window title
window.title("Simple Calculator")

# Create an Entry widget for user input
entry = tk.Entry(window)
entry.pack()

# Create a Label widget to display the result
result_label = tk.Label(window, text="Result: ")
result_label.pack()

# Create a function to perform the calculation
def calculate():
    try:
        # Get the user input from the Entry widget
        expression = entry.get()
        # Evaluate the expression and update the result label
        result_label.config(text="Result: " + str(eval(expression)))
    except Exception as e:
        result_label.config(text="Error: " + str(e))

# Create a Button widget to trigger the calculation
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.pack()

# Start the Tkinter event loop
window.mainloop()
