def Split(list):
  odd_list = []
  for i in list:
    if (i % 2 != 0):
      odd_list.append(i)  
  return odd_list
