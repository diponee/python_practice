def make_pancake(flour, eggs, milk):
  total_pancakes = min(flour * 4, eggs * 4, milk * 4)
  print(f"The number of pancakes you can make is {total_pancakes}")
  
def get_int_input(prompt):
  while True:
    try:
      return int(input(prompt))
    except ValueError:
      print("Please enter a valid integer")
      
flour =get_int_input("Enter the number of flour (in cups): ")
eggs = get_int_input("Enter the number of eggs (in pieces): ")
milk = get_int_input("Enter the number of milk (in cups): ")
make_pancake(flour, eggs, milk)