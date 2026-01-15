import random
print("Welcome to Knowledge Play Zone!")
playing = input("Do you want to play? ")
if playing.lower() != "yes":
  quit()
print("Let's do this")
score = 0
questions = [
  ("What is the full meaning of CPU?", "central processing unit"),
  ("What is the full meaning of GPU?", "graphics processing unit"),
  ("What is the full meaning of RAM?", "random access memory"),
  ("What is the full meaning of ROM?", "read only memory")
]

random.shuffle(questions)

for question, correct_answer in questions:
  answer = input(question + " ")
  if answer.lower() == correct_answer:
    print("Correct!")
    score += 1
  else:
    print("Wrong! Move to the next question.")
print(f"You got {score} out of 4 questions correct")
print("You got " + str((score)/4 * 100) + "% of the questions correctly")

import random
print("Welcome to Tech Knowledge Play Zone!")
playing = input("Do you want to play? ")
if playing.lower() != "yes":
  quit(f"Sad to see you go. See you some other time.")
print("Let's do this")
score = 0
questions = [
  ("What is the full meaning of CPU?", "central processing unit"),
  ("What is the full meaning of GPU?", "graphics processing unit"),
  ("What is the full meaning of RAM?", "random access memory"),
  ("What is the full meaning of SSD?", "solid state drive"),
  ("What is the full meaning of PSU?", "power supply unit"),
  ("What is the full meaning of ROM?", "read only memory")
]

random.shuffle(questions)

for index, (question, correct_answer) in enumerate(questions):
    answer = input(question + " ")
    if answer.lower() == correct_answer:
      print("Correct!")
      score += 1
    else:
        # Print "Wrong!" and check if it's the last question
      if index < len(questions) - 1:
        print("Wrong! Move to the next question.")
      else:
        print("Wrong!")
print(f"You got {score} out of {len(questions)} questions correct.")
print(f"You got {score / len(questions) * 100:.2f}% of the questions correct.")