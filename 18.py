def remove_dirty_chars(string, second_string):
    str_list = list(string)
    for i in second_string:
        while i in str_list:
            str_list.remove(i)
    return "".join(str_list)
