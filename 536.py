def nth_items(list,n):
    new_list = []
    for i in range(len(list)):
        if i % n == 0:
            new_list.append(list[i])
    return new_list
