def multiple_split(text):
    result = []
    temp = ''
    for i in text:
        if i in [';', ',', '*', '\n']:
            if temp:
                result.append(temp)
            temp = ''
        else:
            temp+=i
    if temp:
        result.append(temp)
    return result
