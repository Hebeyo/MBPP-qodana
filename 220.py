def replace_max_specialchar(text,n):
    count = 0
    text = list(text)
    for i in range(len(text)):
        if (text[i] == ' ' or text[i] == ',' or text[i] == '.'):
            if (count < n):
                text[i] = ':'
                count += 1
            else:
                break
    return ''.join(text)
