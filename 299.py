def max_aggregate(stdata):
    temp = {}
    for name, marks in stdata:
        if name not in temp:
            temp[name] = marks
        else:
            temp[name] += marks
    max_aggregate = max(temp, key=temp.get)
    return (max_aggregate, temp[max_aggregate])
