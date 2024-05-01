def remove_odd(l):
    i = 0
    while i < len(l):
        if l[i] % 2 != 0:
            l.pop(i)
        else:
            i += 1
    return l
