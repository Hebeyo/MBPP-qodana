def max_Abs_Diff(arr,n):
    max_diff = 0
    for i in range(n):
        for j in range(n):
            if abs(arr[i] - arr[j]) > max_diff:
                max_diff = abs(arr[i] - arr[j])
    return max_diff
