print("Welcome to the course result checker")
input("Enter the course code: ")
def grade_checker(score):  
  if score < 0 or score > 100:
    print("Invalid Score. Enter a valid score")
  elif score >= 70:
    print ("Grade: A")
  elif score >= 60:
    print ("Grade: B")
  elif score >= 50:
    print ("Grade: C") 
  elif score >= 45:
    print ("Grade: D")
  else:
    print ("Grade: F")
    
# score = input("Enter your score: ")
# if score.isdigit():
#   score = int(score)
#   grade_checker(score)
# else:
#   print("Invalid input. Enter a valid score")

def get_valid_input(prompt):
  while True:
    try:
      return float(input(prompt))
    except ValueError:
      print("Enter a valid number")
score = get_valid_input("Enter your score: ")
grade_checker(score) 








  