def count_word_frequency(text, word):
  words = text.lower().split()
  count = words.count(word.lower())
  return count

text = input("Enter the text you want to check: ")
word_to_count = input("What is the word you want to check: ")

result = count_word_frequency(text, word_to_count)
print(f'The word "{word_to_count}" appears {result} times in the sentence.')
