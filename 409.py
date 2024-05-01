def min_product_tuple(list1):
    result_min = min([abs(x[0]*x[1]) for x in list1] )
    return result_min
