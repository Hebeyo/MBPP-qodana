def merge(lst):
    result = []
    for i in range(len(lst[0])):
        temp = []
        for j in range(len(lst)):
            temp.append(lst[j][i])
        result.append(temp)
    return result
