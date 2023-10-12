def isSmall(list_number):
    min_number = list_number[0]
    for next_number in list_number:
        if next_number < min_number:
            min_number = next_number
    return min_number


print(isSmall(list_number = [10,111,10,19173,9,888,100]))