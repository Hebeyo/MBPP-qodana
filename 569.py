def sort_sublists(list1):
    result = []
    for i in range(len(list1)):
        list1[i] = sorted(list1[i])
        result.append(list1[i])
    return result
