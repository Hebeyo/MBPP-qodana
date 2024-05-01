def check_occurences(test_list):
    res = {} 
    for ele in test_list:
        ele = tuple(sorted(ele))
        if ele in res:
            res[ele] += 1
        else:
            res[ele] = 1
    return (res)
