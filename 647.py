def split_upperstring(text):
    result = ''
    for i in text:
        if i.isupper():
            result += ' ' + i
        else:
            result += i
    return result.split()
