def cheap_items(items,n):
  res = []
  for i in range(n):
    min = 100000
    for j in range(len(items)):
      if items[j]['price'] < min:
        min = items[j]['price']
        index = j
    res.append(items[index])
    items.pop(index)
  return res
