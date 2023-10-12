def Anitclockwise(list_number, start, end):
    while (start < end):
        temp = list_number[start]
        list_number[start] = list_number[end]
        list_number[end] = temp
        start += 1
        end = end-1

def rotation_array_num(list_number, rotate):
    length = len(list_number)
    Anitclockwise(list_number, 0, rotate-1)
    #Anitclockwise(list_number, rotate, length-1)
    #Anitclockwise(list_number, 0, length-1)
    return list_number

list_number = [1,2,3,4]
print(rotation_array_num(list_number, 1))
