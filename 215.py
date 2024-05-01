def decode_list(alist):
    result = []
    for i in alist:
        if isinstance(i, list):
            result.extend(i[0]*[i[1]])
        else:
            result.append(i)
    return result
