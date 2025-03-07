#tire_volume activity


import math  # Import math module for π

# Display message to the user
print("This program calculates the volume of a tire based on its dimensions.")

# Get input from the user
width = float(input("Enter the width of the tire in mm ; "))
aspect_ratio = float(input("Enter the aspect ratio of the tire ; "))
diameter = float(input("Enter the diameter of the wheel in inches ; "))

# Compute the volume using the formula
volume = (math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000

# Display the calculated volume , leaving final values in litres
print(f"\nThe volume of the tire is approximately {volume:.2f} liters.")

# Display a message thanking the user for using the program
print("\nThank you for using this program!")