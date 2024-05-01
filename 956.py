def split_list(text):
  res = []
  temp = ''
  for i in range(len(text)):
    if text[i].isupper():
      res.append(temp)
      temp = ''
    temp += text[i]
  res.append(temp)
  res.remove('')
  return res
