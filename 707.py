def count_Set_Bits(n) :  
    cnt = 0
    for i in range(1, n + 1) : 
        cnt += bin(i).count('1')
    return cnt
