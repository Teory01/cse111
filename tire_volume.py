#tire_volume activity


#import math  # Import math module for π

# Display message to the user
#print("This program calculates the volume of a tire based on its dimensions.")

# Get input from the user
#width = float(input("Enter the width of the tire in mm ; "))
#aspect_ratio = float(input("Enter the aspect ratio of the tire ; "))
#diameter = float(input("Enter the diameter of the wheel in inches ; "))

# Compute the volume using the formula
#volume = (math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000

# Display the calculated volume , leaving final values in litres
#print(f"\nThe volume of the tire is approximately {volume:.2f} liters.")

# Display a message thanking the user for using the program
#print("\nThank you for using this program!")

import math
from datetime import datetime

def calculate_tire_volume(width, aspect_ratio, diameter):
    """Computes the approximate volume of air inside a tire."""
    return (math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000

# Display program title
print("\nTIRE VOLUME CALCULATION")
print("=" * 30)

try:
    # Get user input
    width = float(input("Enter the width of the tire in mm : "))
    aspect_ratio = float(input("Enter the aspect ratio of the tire : "))
    diameter = float(input("Enter the diameter of the wheel in inches : "))

    # Compute volume
    volume = calculate_tire_volume(width, aspect_ratio, diameter)

    # Display results
    print("\nRESULTS")
    print("-" * 30)
    print(f"Tire Width       : {width:.1f} mm")
    print(f"Aspect Ratio     : {aspect_ratio:.1f}")
    print(f"Wheel Diameter   : {diameter:.1f} inches")
    print(f"Tire Volume      : {volume:.2f} liters")
    print("=" * 30)

    # Get the current date (without time)
    current_date = datetime.now().strftime("%Y-%m-%d")

    # Append data to the volumes.txt file
    with open("volumes.txt", "a") as file:
        file.write(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}\n")

    print("\nData has been saved to 'volumes.txt'. Thank you!\n")

except ValueError:
    print("\nError: Please enter valid numeric values.\n")
