def checkSecondLargestElement(list_number):
    list_number.sort()
    return list_number[-2]


print(checkSecondLargestElement([10,8,1,5,3,5]))