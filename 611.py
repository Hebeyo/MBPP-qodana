def max_of_nth(test_list, N):
  res = 0
  for i in test_list:
    if i[N] > res:
      res = i[N]
  return (res)
