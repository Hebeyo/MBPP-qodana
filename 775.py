def odd_position(nums):
    for i in range(len(nums)):
        if i%2 != 0 and nums[i]%2 == 0:
            return False
    return True
