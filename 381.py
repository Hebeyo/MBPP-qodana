def index_on_inner_list(list_data, index_no):
    result = sorted(list_data, key=lambda x: x[index_no])
    return result
