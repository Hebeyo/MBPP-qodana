def check(n):
    num = n
    rev_num = 0
    while (n > 0):
        rev_num = (rev_num * 10 + n % 10)
        n = n // 10
    return (2 * rev_num == num + 1)
