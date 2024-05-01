def remove_duplicate(list1):
    list1.sort()
    remove_duplicate = []
    for i in list1:
        if i not in remove_duplicate:
            remove_duplicate.append(i)
    return remove_duplicate
