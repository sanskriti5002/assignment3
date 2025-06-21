# Task 2: Using the Math Module for Calculations
 
# Problem Statement: Write a Python program that:
# 1.   Asks the user for a number as input.
# 2.   Uses the math module to calculate the:
# o   Square root of the number
# o   Natural logarithm (log base e) of the number
# o   Sine of the number (in radians)
# 3.   Displays the calculated results.
#  Expected Output:
#  For example, if the user enters 25, the output should be:


import math

number = float(input("Enter a number:"))
square_root = math.sqrt(number)

if number > 0 :
    natural_log = math.log(number)
else:
    natural_log = "Undefined(log of non-positive number)"

sine_value = math.sin(number)

print("\nResults:")
print("\nSquare root:", square_root)
print("Natural logarithm:", natural_log)
print("Sin(in radians):", sine_value)
