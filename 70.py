def get_equal(Input, k):
  flag = 1
  for tuple in Input:
    if len(tuple) != k:
      flag = 0
      break
  if flag == 1:
    return ("All tuples have same length")
  else:
    return ("All tuples do not have same length")
