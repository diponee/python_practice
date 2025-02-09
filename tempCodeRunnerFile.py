def is_palindrome(word):
  return word == word[::-1]
word = input("Enter the word you want to check: ").strip().lower()
if is_palindrome(word):
  print("The word is a palindrome.")
else:
  print("The word is not a palindrome.")