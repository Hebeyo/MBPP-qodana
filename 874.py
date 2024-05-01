def check_Concat(str1,str2):
    if len(str1) % len(str2) != 0:
        return False
    for i in range(len(str1)):
        if str1[i] != str2[i % len(str2)]:
            return False
    return True
