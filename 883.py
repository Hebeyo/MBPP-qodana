def div_of_nums(nums,m,n):
    result = []
    for i in nums:
        if i % m == 0 and i % n == 0:
            result.append(i)
    return result
