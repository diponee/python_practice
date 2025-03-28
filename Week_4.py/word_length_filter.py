def filter_word_length(words):
  return len(words) >= 4

try:
  user_input = input("Enter a list of words separated by spaces: ")
  words = user_input.split()
  filtered_words = list(filter(filter_word_length, words))
  print(f'Words with 4 or more letters in the list are {filtered_words}')
except ValueError:
  print('Invalid input')