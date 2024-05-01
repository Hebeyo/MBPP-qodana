def extract_string(str, l):
    res = []
    for e in str:
        if len(e) == l:
            res.append(e)
    return res
