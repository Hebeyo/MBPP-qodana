def count_duplic(lists):
    if not lists:
        return [],[]
    element = [lists[0]]
    frequency = [1]
    for i in range(1,len(lists)):
        if lists[i] == lists[i-1]:
            frequency[-1] += 1
        else:
            element.append(lists[i])
            frequency.append(1)
    return element,frequency
