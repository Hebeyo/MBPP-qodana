def maximize_elements(test_tup1, test_tup2):
  res = []
  for i in range(len(test_tup1)):
    res.append(tuple(max(test_tup1[i][j], test_tup2[i][j]) for j in range(len(test_tup1[i])))
    )
  return (tuple(res))
