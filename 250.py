def count_X(tup, x):
    count = 0
    for i in range(len(tup)):
        if tup[i] == x:
            count += 1
    return count
