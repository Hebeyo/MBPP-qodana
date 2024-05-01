def round_and_sum(list1):
  for i in range(len(list1)):
    list1[i]=round(list1[i])
  round_and_sum=sum(list1)*len(list1)
  return round_and_sum
