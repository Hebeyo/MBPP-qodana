def num_comm_div(x, y):
    result = 0
    for i in range(1, min(x, y) + 1):
        if x % i == y % i == 0:
            result += 1
    return result
