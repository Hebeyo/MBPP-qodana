def Odd_Length_Sum(arr):
    Sum = 0
    for i in range(len(arr)):
        for j in range(i,len(arr),2):
            Sum += sum(arr[i:j+1])
    return Sum
