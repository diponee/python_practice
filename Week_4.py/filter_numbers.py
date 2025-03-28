# Write a program that accepts a list of numbers and filters out the odd numbers using the filter() function

def is_even (num):
  return num % 2 == 0

user_input = input("Enter a list of numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))

even_numbers = list(filter(is_even, numbers))

print(f"The even numbers in the list are:", even_numbers)

# Write a program that accepts a list of numbers and filters out the even numbers using the filter() function
def is_odd (num):
  return num % 2 == 1

user_input = input("Enter a list of numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))

odd_numbers = list(filter(is_odd, numbers))

print(f"The odd numbers in the list are:", odd_numbers)