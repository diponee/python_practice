# Sum of Even Numbers
# Create a Python program that calculates the sum of all even numbers between 1 and 50 using a for loop.

# Hint: Use the range() function with steps of 2 to iterate over even numbers.
# Expected Output Example:
# "The sum of even numbers from 1 to 50 is 650

even_sum = 0

for num in range (0, 51, 2):
  
  even_sum += num
  
print (f"The sum of all even numbers between 0 and 50 is: {even_sum}")