print("Welcome to Discount Hub Stores")
def calculate_discount(initial_price, discount_percentage):
  discount_price = initial_price * (discount_percentage / 100)
  final_price = initial_price - discount_price
  print(f"The price after a {discount_percentage}% discount is: {final_price} naira")

def get_valid_number(prompt):
  while True:
    try:
      return float(input(prompt))
    except ValueError:
      print("Enter a valid number")
    
initial_price = get_valid_number("Enter the initial price of your item: ")
discount_percentage = get_valid_number("Enter the percentage discount on the item: ")
calculate_discount(initial_price, discount_percentage)