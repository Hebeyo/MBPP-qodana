def merge_sorted_list(num1,num2,num3):
  result = []
  for i in num1:
    result.append(i)
  for i in num2:
    result.append(i)
  for i in num3:
    result.append(i)
  result.sort()
  return result
