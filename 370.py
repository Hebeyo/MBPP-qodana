def float_sort(price):
  price.sort(key=lambda x: float(x[1]), reverse=True)
  return price
