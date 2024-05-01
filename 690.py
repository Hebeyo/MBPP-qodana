def mul_consecutive_nums(nums):
    result = []
    for i in range(1,len(nums)):
        result.append(nums[i]*nums[i-1])
    return result
