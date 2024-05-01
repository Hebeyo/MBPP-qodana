def check_type(test_tuple):
  res = True
  for ele in test_tuple:
    if type(ele) != type(test_tuple[0]):
      res = False
      break
  return (res)
