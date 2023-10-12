def is_Monotonic(list_number):
    ascending_list = []
    desending_list = []
    ascending_list.extend(list_number)
    desending_list.extend(list_number)

    ascending_list.sort()
    desending_list.sort(reverse=True)

    if ascending_list == list_number or desending_list == list_number:
        return True
    else:
        return False


