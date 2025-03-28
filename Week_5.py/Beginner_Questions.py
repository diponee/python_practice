# Error Handling In Python

# Write a function divide_numbers(a, b) that returns the result of a / b. Handle the case where b is zero by returning "Cannot divide by zero"

def divide_numbers (a, b):
  try:
    return round(a/b, 2) #The round is to round-up the answers to 2
  except ZeroDivisionError:
    return "Cannot divide by zero"
try:  
  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))
  result = divide_numbers(num1, num2)
  print(f"Result: {result}")
except:
  print("Invalid input!! Enter a valid numeric value")
  

# Write a program that reads an integer input from the user. Use a try-except block to handle Value Error if the user enters invalid data (e.g., a string like "abc")

try:
    num = int(input("Enter an integer: "))  # Read input and convert to integer
    print(f"You entered: {num}")
except ValueError:
    print("Invalid input! Please enter a valid integer.")
    
    
# Write a small program that prompts the user for their age (as an integer) and uses a try-except block to handle ValueError in case the user inputs a non-integer (e.g., "twenty")

try:
    age = int(input("Enter your age: "))
    print(f'You are {age} years old')
except:
    print("Invalid input! Enter your age in numbers only")
