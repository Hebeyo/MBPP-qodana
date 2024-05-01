def round_num(n,m):
    a = (n //m) * m
    b = a + m
    if n - a > b - n:
        return b
    else:
        return a
