def first_non_repeating_character(str1):
  for i in range(len(str1)):
    found = False
    for j in range(len(str1)):
      if i != j and str1[i] == str1[j]:
        found = True
        break
    if not found:
      return str1[i]
  return None
