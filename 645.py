def find_k_product(test_list, K):
  res = 1
  for i in test_list:
    res *= i[K]
  return (res)
