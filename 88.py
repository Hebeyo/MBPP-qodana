def freq_count(list1):
  freq_count= {}
  for item in list1:
    if item in freq_count:
      freq_count[item] += 1
    else:
      freq_count[item] = 1
  return freq_count
