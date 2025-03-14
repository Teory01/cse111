"""
You work for a retail store that wants to increase sales on Tuesday
and Wednesday, which are the store's slowest sales days. On Tuesday
and Wednesday, if a customer's subtotal is greater than $50, the
store will discount the customer's purchase by 10%.
"""

# Import the datatime module so that it can be used in this program.
from datetime import datetime

# The discount rate is 10% and the sales tax rate is 6%.
DISCOUNT_RATE = 0.10
SALES_TAX_RATE = 0.06

subtotal = 0

print("Enter the price and quantity for each item.")
price = 1
while price != 0:
    price = float(input("Please enter the price: "))
    if price != 0:
        # Get the quantity from the user.
        quantity = int(input("Please enter the quantity: "))
        subtotal += price * quantity
        print()

# Round the subtotal to a whole number
subtotal = round(subtotal, 2)
print(f"Subtotal: {subtotal:.2f}")
print()

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()

# Call the weekday() method to get the day of the week from the current_date_and_time object.
weekday = current_date_and_time.weekday()

# if the subtotal is greater than 50 and today is Tuesday or Wednesday, compute the discount amount.
if weekday == 1 or weekday == 2:
    if subtotal < 50:
        lacking = 50 - subtotal
        print("To receive the discount, add"
                f" {lacking:.2f} to your order.")
    else:
        discount = round(subtotal * DISCOUNT_RATE, 2)
        print(f"Discount amount: {discount:.2f}")
        subtotal -= discount

# Compute the sales tax. Notice that we compute the sales tax
# after computing the discount because the customer does not
# pay sales tax on the full price but on the discounted price.
sales_tax = round(subtotal * SALES_TAX_RATE, 2)
print(f"Sales tax amount: {sales_tax:.2f}")

# Compute the total by adding the subtotal and the sales tax.
total = subtotal + sales_tax

# Display the total for the user to see.
print(f"Total: {total:.2f}")
