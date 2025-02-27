def capitalize_languages(languages):
    """Capitalize each string in the list."""
    return list(map(str.capitalize, languages))

# Input from the user
languages_input = input("Enter programming languages separated by commas (e.g., python, java, c++): ")

# Convert the input string into a list
languages = languages_input.split(',')

# Stripping any leading/trailing whitespace from each language
languages = [lang.strip() for lang in languages]

# Capitalizing the languages
capitalized_languages = capitalize_languages(languages)

# Output the result
print(capitalized_languages)