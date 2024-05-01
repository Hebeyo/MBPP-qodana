def max_sum_list(lists):
    max_sum = 0
    max_list = []
    for l in lists:
        if sum(l) > max_sum:
            max_list = l
            max_sum = sum(l)
    return max_list
