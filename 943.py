def combine_lists(num1,num2):
  from heapq import merge
  combine_lists=list(merge(num1, num2))
  return combine_lists
