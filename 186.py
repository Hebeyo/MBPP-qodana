def check_literals(text, patterns):
  for pattern in patterns:
    if pattern in text:
      return ('Matched!')
    else:
      return ('Not Matched!')
