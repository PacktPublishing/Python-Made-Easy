global_variable = 10

def my_function():
    local_variable = 20
    print(global_variable)  # Access global variable
    print(local_variable)   # Access local variable

my_function()
print(global_variable)      # Access global variable
print(local_variable)       # Error: Local variable  not accessible outside my_function







