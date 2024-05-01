def average_Odd(n):
    result = 0
    count = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            result += i
            count += 1
    return result // count
