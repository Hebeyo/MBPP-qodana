def extract_singly(test_list):
  res = []
  for inner in test_list:
    for ele in inner:
      if inner.count(ele) == 1 and ele not in res:
        res.append(ele)
  return (res)
