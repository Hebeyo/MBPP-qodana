def sort_counter(dict1):
    x = dict1
    sort_counter=sorted(x.items(), key=lambda x: x[1], reverse=True)
    return sort_counter
