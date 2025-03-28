expression = input("Enter a mathematical expression: ")

try:
  result = round(eval(expression), 2)
  print(f'The result of the expression "{expression}" is: {result}')
except Exception as e:
  print(f"Error evaluating the expression: {e}")