def first_Element(arr,n,k): 
    for i in range(0, n): 
        count = 0
        for j in range(0, n): 
            if (arr[i] == arr[j]): 
                count += 1
        if (count == k): 
            return arr[i] 
    return -1
