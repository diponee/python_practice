# Function to round a floating-point number to 2 decimal places
def round_to_two_decimal_places(float_number):
  return round(float_number, 2)

try:
  float_number = float(input("Enter a floating-point number: "))
  # Rounding the number
  rounded_number = round_to_two_decimal_places(float_number)
  # Output the result
  print(f'The number rounded to 2 decimal places is: {rounded_number}')
except ValueError:
  print("Invalid input! Please enter a valid float number.")