def heap_queue_largest(nums,n):
  largest_nums = []
  for i in range(n):
    largest_nums.append(max(nums))
    nums.remove(max(nums))
  return largest_nums
