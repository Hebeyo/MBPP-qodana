def get_max_occuring_char(str1):
    max = -1
    ch = ''
    for i in str1:
        count = str1.count(i)
        if count > max:
            max = count
            ch = i
    return ch
