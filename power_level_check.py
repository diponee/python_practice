def can_fly(power_level):
  if power_level >= 100:
    return "You can fly!"
  else:  
    return "Try again, keep training!"

# Test the function
try:
    power_level = int(input("Enter your power level: "))
    result = can_fly(power_level)
    print(result)
except ValueError:
    print("Invalid input! Please enter a numeric power level.")
    

def length_of_word(word):
  return len(word)

word = input("Enter your preferred word: ").lower().strip()
if word:
  result = length_of_word(word)
  print(f"The length of the word is: {result}")
else:
  print("You entered an empty string. Please enter a valid word.")
