def generate_matrix(n):
    if n==0:
        return []
    if n==1:
        return [[1]]
    matrix = [[0 for i in range(n)] for j in range(n)]
    row_start = 0
    row_end = n-1
    col_start = 0
    col_end = n-1
    num = 1
    while row_start <= row_end and col_start <= col_end:
        for i in range(col_start, col_end+1):
            matrix[row_start][i] = num
            num += 1
        row_start += 1
        for i in range(row_start, row_end+1):
            matrix[i][col_end] = num
            num += 1
        col_end -= 1
        for i in range(col_end, col_start-1, -1):
            matrix[row_end][i] = num
            num += 1
        row_end -= 1
        for i in range(row_end, row_start-1, -1):
            matrix[i][col_start] = num
            num += 1
        col_start += 1
    return matrix
