def find_character(string):
  uppercase_characters = []
  lowercase_characters = []
  numerical_characters = []
  special_characters = []
  for i in string:
    if i.isupper():
      uppercase_characters.append(i)
    elif i.islower():
      lowercase_characters.append(i)
    elif i.isdigit():
      numerical_characters.append(i)
    else:
      special_characters.append(i)
  return uppercase_characters, lowercase_characters, numerical_characters, special_characters
