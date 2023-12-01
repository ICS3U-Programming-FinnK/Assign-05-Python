#!/usr/bin/env python3
# Created By: Finn Kitor
# Date: December 1st, 2023
# This program asks the user for the subtotal and the tax in precentage


# Function: tax. Parameters: subtotal, and total. (both float)
def tax(subtotal: float, total: float) -> float:
    # Checking if the subtotal or total is negative
    if subtotal < 0 or total < 0:
        raise ValueError("Error: you inputted a negative number .")

    # Calculating the tax percentage
    tax_percentage = ((total - subtotal) / subtotal) * 100

    return tax_percentage


# Def main function
def main():
    try:
        # Getting input from the user
        subtotal = float(input("Please enter the subtotal in CAD$: "))
        total = float(input("Please enter the total cost in CAD$: "))

        # Calculating the tax percentage
        tax_percentage = tax(subtotal, total)

        # Displaying the tax percentage to the user
        print(f"The tax percentage is: {tax_percentage}%")
    # Invalid input response to the user
    except ValueError as e:
        print(f"Error: Invalid input: {e}")


if __name__ == "__main__":
    main()
