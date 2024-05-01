def dig_let(s):
    digit=0
    letter=0
    for i in s:
        if i.isdigit():
            digit+=1
        elif i.isalpha():
            letter+=1
    return (letter,digit)
