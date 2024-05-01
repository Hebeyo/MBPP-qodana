def remove_splchar(text):
  result = ''
  for char in text:
    if char.isalnum():
      result += char
  return result
