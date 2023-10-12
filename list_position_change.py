def swapPosition(list_numbers, pos1, pos2):
    temp = list_numbers[pos1]
    list_numbers[pos1]=list_numbers[pos2]
    list_numbers[pos2]=temp
    return list_numbers

def swapMath(list_numbers, pos1, pos2):
    list_numbers[pos1]= list_numbers[pos1]+ list_numbers[pos2]   
    list_numbers[pos2]=list_numbers[pos1]-list_numbers[pos2]   
    list_numbers[pos1]=list_numbers[pos1]-list_numbers[pos2]
    return list_numbers  

print("SwapPosition = ",swapPosition([1,2,3,4], 1, 3))
print("SwapMath = ",swapMath([1,2,3,4], 1, 3))

