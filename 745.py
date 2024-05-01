def divisible_by_digits(startnum, endnum):
    result = []
    for i in range(startnum,endnum+1):
        str_i = str(i)
        for j in str_i:
            if j == '0' or i % int(j) != 0:
                break
        else:
            result.append(i)
    return result
