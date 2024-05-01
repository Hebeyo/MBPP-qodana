def Repeat(x):
    size = len(x)
    repeated = []
    for i in range(size):
        for j in range(i+1, size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated
