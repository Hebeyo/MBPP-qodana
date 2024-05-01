def adjacent_num_product(list):
  max_product = 0
  for i in range(len(list)-1):
    product = list[i] * list[i+1]
    if product > max_product:
      max_product = product
  return max_product
