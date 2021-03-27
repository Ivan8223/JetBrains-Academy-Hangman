def find_my_list(lists, my_list):
    for lst_index, lst in enumerate(lists):
        if id(lst) == id(my_list):
            return lst_index
    return None
