# Write a program to count how many numbers between 1 and 1000 are divisible
# by both 7 and 11.

divisible_num = 0

for num in range (1, 1001):
  
  if num % 7 == 0 and num % 11 == 0:
    
    divisible_num += 1
  
print(f"there are {divisible_num} numbers between 1 and 1000 that are divisible by 7 and 11")