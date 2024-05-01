def replace(string, char):
    str = list(string)
    i = 0
    while(i < len(str)):
        if(str[i] == char):
            j = i + 1
            while(j < len(str) and str[j] == char):
                j = j + 1
            if(j - i > 1):
                del str[i + 1:j]
        i = i + 1
    return "".join(str)
