def most_occurrences(test_list):
  wrd = {}
  for sub in test_list:
    for word in sub.split():
      if word not in wrd:
        wrd[word] = 1
      else:
        wrd[word] += 1
  max_occ = max(wrd, key=wrd.get)
  return max_occ
