def unique_Characters(str):
    str1 = ""
    for i in str:
        if i not in str1:
            str1 += i
        else:
            return False
    return True
