def pack_consecutive_duplicates(list1):
    res = []
    temp = [list1[0]]
    for i in range(1, len(list1)):
        if list1[i] == list1[i - 1]:
            temp.append(list1[i])
        else:
            res.append(temp)
            temp = [list1[i]]
    res.append(temp)
    return res
