def grouping_dictionary(l):
    d = {}
    for k, v in l:
        if k in d:
            d[k].append(v)
        else:
            d[k] = [v]
    return d
