def find_mystery_number(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0] 
    if even_numbers: 
      return max(even_numbers)
    else:
      return "No even numbers found!"
try:
    input_numbers = input("Enter a list of numbers separated by spaces: ").strip()
    numbers_list = list(map(int, input_numbers.split()))
    result = find_mystery_number(numbers_list)
    print(result)
except ValueError:
    print("Invalid input! Please enter numbers only.")
