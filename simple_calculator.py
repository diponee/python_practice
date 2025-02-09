def add_two_numbers(num1, num2):
  sum_result = num1 + num2
  print(f"The sum of the two numbers is {sum_result}")
def get_valid_number(prompt):
  while True:
    try:
      return float(input(prompt)) 
    except ValueError:
      print("Invalid input! Please enter a valid number.")
num1 = get_valid_number ("Enter the first number: ")
num2 = get_valid_number ("Enter the second number: ")
add_two_numbers(num1, num2)