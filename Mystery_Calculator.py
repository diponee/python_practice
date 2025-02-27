def mystery_calculation(a, b, c):
  mystery_calculation = ((a + b) * c) / 2
  print(f"The final answer to our mystery calculator is {mystery_calculation}")
  
def get_valid_input(prompt):
  while True:
    try:
      return float(input(prompt))
    except ValueError:
      print('Enter a valid number.')
    
a = get_valid_input("Enter the first number: ")
b = get_valid_input("Enter the second number: ")
c= get_valid_input("Enter the third number: ")
mystery_calculation(a, b, c)
