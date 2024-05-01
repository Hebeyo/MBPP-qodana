def dif_Square(n):
    for i in range(1,n):
        for j in range(1,n):
            if (i*i - j*j) == n:
                return True
    return False
