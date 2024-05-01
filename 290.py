def max_length(list1):
    max_length = 0
    max_list = []
    for i in list1:
        if len(i) > max_length:
            max_length = len(i)
            max_list = i
    return (max_length, max_list)
