def reverse_list_lists(lists):
    for i in range(len(lists)):
        lists[i].sort(reverse = True)
    return lists
