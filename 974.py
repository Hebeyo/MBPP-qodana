def min_sum_path(A): 
    for i in range(len(A) - 2, -1,-1): 
        for j in range( len(A[i])): 
            A[i][j] += min(A[i + 1][j], 
                            A[i + 1][j + 1]) 
    return A[0][0]
