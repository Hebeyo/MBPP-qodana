def large_product(nums1, nums2, N):
    result = []
    for i in nums1:
        for j in nums2:
            result.append(i*j)
    result.sort(reverse=True)
    return result[:N]
