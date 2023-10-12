def find_two_largest_element(listnumber, search):
    listnumber.sort()
    return listnumber[-search:]


print(find_two_largest_element([10,2,1,3,45], 2))




