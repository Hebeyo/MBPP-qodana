def sum_Square(n):
    for i in range(1, n):
        for j in range(1, n):
            if (i**2 + j**2 == n):
                return True
    return False
