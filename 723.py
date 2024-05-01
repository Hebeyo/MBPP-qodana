def count_same_pair(nums1, nums2):
    result = 0
    for i in range(len(nums1)):
        if nums1[i] == nums2[i]:
            result += 1
    return result
