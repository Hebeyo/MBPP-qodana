def heap_queue_smallest(nums,n):
  import heapq as hq
  hq.heapify(nums)
  smallest_nums = [hq.heappop(nums) for _ in range(n)]
  return smallest_nums
