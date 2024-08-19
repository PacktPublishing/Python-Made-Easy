# Prompt the user to enter the weight of the package in kilograms and convert it to a float
weight = float(input("Enter the weight of the package in kilograms: "))

# Prompt the user to enter the destination (domestic or international)
destination = input("Enter the destination (domestic or international): ")


if weight <= 0:                                   # Check if the weight is less than or equal to zero
    print("Invalid weight.")                      # Display an error message for invalid weight

elif destination == "domestic":                   # Check if the destination is "domestic"

    if weight <= 1:                               # Check the weight range for domestic shipping costs
        print("Shipping cost: $5")
    elif weight <= 5:
        print("Shipping cost: $10")
    elif weight <= 10:
        print("Shipping cost: $15")
    else:
        print("Shipping cost: $20")

elif destination == "international":             # Check if the destination is "international"

    if weight <= 1:                              # Check the weight range for international shipping costs
        print("Shipping cost: $15")
    elif weight <= 5:
        print("Shipping cost: $25")
    elif weight <= 10:
        print("Shipping cost: $40")
    else:
        print("Shipping cost: $60")

else:                                           # Handle the case where the destination is neither "domestic" nor "international"
    print("Invalid destination.")
