def big_diff(nums):
    max_num = nums[0]
    min_num = nums[0]
    for num in nums:
        max_num = max(max_num, num)
        min_num = min(min_num, num)
    return max_num - min_num
