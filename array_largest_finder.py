def get_max_number(list_num):
    max_number = list_num[0]
    for next_number in list_num:
        if next_number > max_number:
            max_number = next_number
    return max_number
    

print(get_max_number(list_num = [10,111,10,0,19173,9,888,100]))


