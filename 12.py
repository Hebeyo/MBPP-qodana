def sort_matrix(M):
    n = len(M)
    for i in range(n):
        for j in range(n-i-1):
            if sum(M[j]) > sum(M[j+1]):
                M[j], M[j+1] = M[j+1], M[j]
    return M
