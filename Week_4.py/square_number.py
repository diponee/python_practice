# def square_each_number(num):
#   return num ** 2

# try:
#   nums = int(input("Enter the number you want to square: "))
#   square = square_each_number(nums)
#   print(f'The square of {nums} is: {square}')
# except ValueError:
#   print("Invalid inout, enter a valid number")
  
  

def square(num):
  return num ** 2

try:
  user_input = input("Enter a list of numbers separated by spaces: ")
  numbers = list(map(int, user_input.split()))
  squared_numbers = list(map(square, numbers))
  print(f"The square of {numbers} is {squared_numbers}")
except ValueError:
  print("Invalid number, enter a valid number")
  
  
  # Accept user input for a mathematical expression
expression = input("Enter a mathematical expression: ")

try:
  result = round(eval(expression), 2)
  print(f'The result of the expression "{expression}" is: {result}')
except Exception as e:
  print(f"Error evaluating the expression: {e}")