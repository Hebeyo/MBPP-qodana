def split_two_parts(list1, L):
    list2 = []
    list3 = []
    for i in range(L):
        list2.append(list1[i])
    for i in range(L,len(list1)):
        list3.append(list1[i])
    return (list2,list3)
