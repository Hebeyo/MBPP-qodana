def second_frequent(input):
  dict = {}
  for i in input:
    if i in dict:
      dict[i] += 1
    else:
      dict[i] = 1
  max1 = max2 = 0
  for value in dict.values():
    if value > max1:
      max2 = max1
      max1 = value
    elif value > max2:
      max2 = value
  for key in dict:
    if dict[key] == max2:
      return key
  return "No second most frequent string"
