def min_length(list1):
    min_length = len(list1[0])
    min_list = list1[0]
    for i in range(1,len(list1)):
        if len(list1[i]) < min_length:
            min_length = len(list1[i])
            min_list = list1[i]
    return (min_length, min_list)
