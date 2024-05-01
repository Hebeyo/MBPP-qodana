def is_Product_Even(arr,n):
    product = 1
    for i in range(n):
        product *= arr[i]
    if product % 2 == 0:
        return True
    else:
        return False
