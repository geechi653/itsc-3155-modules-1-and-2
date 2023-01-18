original_string = input("Enter a string: ")

lowercase_letters = [c for c in original_string if c.islower()]

uppercase_letters = [c for c in original_string if c.isupper() or c.isspace()]

updated_string = ''.join(lowercase_letters + uppercase_letters)
print("Updated", updated_string)
