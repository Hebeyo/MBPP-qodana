def is_abundant(n):
    fctrsum = 0
    for fctr in range(1, n):
        if n % fctr == 0:
            fctrsum += fctr
    return fctrsum > n
