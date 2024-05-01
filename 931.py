def sum_series(number):
    total = 0
    for i in range(1, number+1):
        total += i*i*i
    return total
