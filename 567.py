def issort_list(list1):
    for i in range(len(list1)-1):
        if list1[i]>list1[i+1]:
            return False
    return True
