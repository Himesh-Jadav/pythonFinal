# Basic exception-handling examples for Lab 10 programs

# Input conversion
try:
    number = int(input("Enter an integer: "))
    print(number)
except ValueError:
    print("Please enter a valid integer.")

# Division
try:
    a = float(input("Enter numerator: "))
    b = float(input("Enter denominator: "))
    print(a / b)
except ValueError:
    print("Please enter numbers.")
except ZeroDivisionError:
    print("Cannot divide by zero.")

# File access
try:
    with open("example.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found.")
except OSError as e:
    print("File error:", e)
