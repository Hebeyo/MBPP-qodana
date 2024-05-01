def consecutive_duplicates(nums):
    res = []
    for i in range(len(nums)-1):
        if nums[i] != nums[i+1]:
            res.append(nums[i])
    res.append(nums[-1])
    return res
