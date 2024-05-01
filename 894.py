def float_to_tuple(test_str):
  res = test_str.split(', ')
  res = [float(i) for i in res]
  res = tuple(res)
  return (res)
