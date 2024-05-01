def unique_product(list_data):
    unique_list = []
    for i in list_data:
        if i not in unique_list:
            unique_list.append(i)
    product = 1
    for i in unique_list:
        product *= i
    return product
