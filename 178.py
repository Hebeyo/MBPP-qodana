def string_literals(patterns,text):
  for pattern in patterns:
    if pattern in text:
      return ('Matched!')
    else:
      return ('Not Matched!')
