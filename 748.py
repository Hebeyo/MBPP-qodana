def capital_words_spaces(str1):
  new_str = ''
  for i in str1:
    if i.isupper():
      new_str += ' ' + i
    else:
      new_str += i
  return new_str.strip()
