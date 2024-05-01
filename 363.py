def add_K_element(test_list, K):
  res = []
  for i in test_list:
    temp = []
    for j in i:
      temp.append(j+K)
    res.append(tuple(temp))
  return (res)
