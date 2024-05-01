def count_Odd_Squares(n,m): 
    count = 0
    for i in range(n,m+1): 
        if (int(i**0.5) - int((i-1)**0.5) == 1): 
            count += 1
    return count
