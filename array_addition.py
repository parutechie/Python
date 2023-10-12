def isremainder_of_an_array(listnumber, divider):
    result = 1
    for eachnumber in listnumber:
        result = (result * eachnumber) #% divider
    return result % divider


print(isremainder_of_an_array([1,2,3,4],5))