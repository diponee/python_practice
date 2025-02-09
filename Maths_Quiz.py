def math_quiz(num1, num2):
  sum_results = (num1 + num2)
  difference_result = (num1 - num2)
  multiply_result = (num1 * num2)
  quotient_results = (num1 /num2) if num2 != 0 else None
  print(f"Addition: {sum_results}, Difference: {difference_result}, Product: {multiply_result}, Division: {quotient_results}")

def get_valid_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Enter a valid number")
num1 = get_valid_number("Enter your first number: ")
num2 = get_valid_number("Enter your second number: ")
math_quiz(num1, num2)


# def calculate_area(shape, dimension1, dimension2):
#     if shape.lower() == 'rectangle':
#         print(dimension1 * dimension2)
#     elif shape.lower() == 'square':
#         print(dimension1 * dimension1)
#     else:
#         print("Error: Shape must be 'rectangle' or 'square'.")
# shape = str(input("What shape do you want to calculate its dimension? "))
# dimension1 = float(input("What is the measurement of the length in metres? "))
# dimension2 = float(input("What is the measurement of the breath in metres? "))
# calculate_area(shape, dimension1, dimension2)

# # Test the function with a rectangle
# rectangle_area = calculate_area('rectangle', 5, 3)
# print(f"Area of rectangle: {rectangle_area}")  # Output: Area of rectangle: 15

# # Test the function with a square
# square_area = calculate_area('square', 4)
# print(f"Area of square: {square_area}")  # Output: Area of square: 16