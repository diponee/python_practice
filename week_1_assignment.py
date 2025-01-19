num_square = {num : num**2 for num in range (1, 6)}
print(num_square)

def isdisjoint(fruits_1, fruits_2):
  return fruits_1.isdisjoint(fruits_2)
fruits_1 = {'Banana', 'Orange', 'PawPaw'}
fruits_2 = {'Apple', 'Cashew', 'Tomato'}
print(isdisjoint(fruits_1, fruits_2))

#Write a program to find all the vowels present in the sentence "Python programming is fun" using a set
def find_vowels(sentence):
  vowels = {'a', 'e', 'i', 'o', 'u'}
  found_vowels = {char for char in sentence.lower() if char in vowels}
  return found_vowels
sentence = "Python programming is fun"
vowels_in_sentence = find_vowels(sentence)
print(f"Vowels in the sentence: {vowels_in_sentence}")
    
    
    
name = input("What is your name: ")
print(f"Hello", name)