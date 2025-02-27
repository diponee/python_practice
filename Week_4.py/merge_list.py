def merge_lists(names, scores):
    """Merge two lists into a list of tuples."""
    return list(zip(names, scores))

# Input from the user
names_input = input("Enter names separated by commas (e.g., John, Jane): ")
scores_input = input("Enter scores separated by commas (e.g., 80, 90): ")

# Convert the input strings into lists
names = names_input.casefold().split(',')
scores = list(map(int, scores_input.split(',')))  # Convert scores to integers

# Merging the lists
merged_list = merge_lists(names, scores)

# Output the result
print(merged_list)