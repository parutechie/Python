def isInterchangeList(list_number):
    temp = list_number[0]
    list_number[0] = list_number[len(list_number) - 1]
    list_number[len(list_number) - 1] = temp
    return list_number


print(isInterchangeList([5,2,3,4]))



