def first_even(nums):
    for num in nums:
        if num % 2 == 0:
            return num
    return -1
