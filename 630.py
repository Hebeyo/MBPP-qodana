def get_coordinates(test_tup):
  res = []
  for i in range(test_tup[0]-1, test_tup[0]+2):
    for j in range(test_tup[1]-1, test_tup[1]+2):
      res.append([i,j])
  return res
