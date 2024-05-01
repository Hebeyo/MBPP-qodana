def check_greater(test_tup1, test_tup2):
  res = []
  for i in range(len(test_tup1)):
    if test_tup2[i] > test_tup1[i]:
      res.append(True)
    else:
      res.append(False)
  return (all(res))
