def average_tuple(nums):
    result = []
    for i in range(len(nums[0])):
        temp = 0
        for j in range(len(nums)):
            temp += nums[j][i]
        result.append(temp/len(nums))
    return result
