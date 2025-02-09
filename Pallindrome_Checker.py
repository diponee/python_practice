# def is_palindrome(word):
#   if word == word[::-1]:
#     print(f"The word is a palindrome")
#   else:
#     print(f"The word is not a palindrome")
    
# word = str(input("Enter the word you want to check: ")).lower()
# is_palindrome(word)


def is_palindrome(word):
  return word == word[::-1]
word = input("Enter the word you want to check: ").strip().lower()
if is_palindrome(word):
  print("The word is a palindrome.")
else:
  print("The word is not a palindrome.")