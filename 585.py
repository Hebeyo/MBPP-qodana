def expensive_items(items,n):
  res = []
  for i in range(n):
    max = 0
    for j in range(len(items)):
      if items[j]['price'] > max:
        max = items[j]['price']
        index = j
    res.append(items[index])
    items.pop(index)
  return res
