import random
correct_number = random.randint(0, 20) 
attempts = 0
max_attempts = 5

print('Guess a number between 1 and 20: ')
while attempts < max_attempts:
  guess = input()
  if guess.isdigit():
    guess = int(guess)
    if guess == correct_number:
      print('Congratulations! You guessed right!')
      break
    elif guess< correct_number:
      print("Too low! Try again. Enter another number")
    else:
      print("Too high! Try again. Enter another number")
    attempts += 1
  else:
    print("Try again. Enter a valid number")
if attempts == max_attempts:
  print("Game Over. The correct number is:",correct_number)
      