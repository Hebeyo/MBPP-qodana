def two_unique_nums(nums):
  result = []
  for i in nums:
    if nums.count(i) == 1:
      result.append(i)
  return result
