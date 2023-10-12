def isEven(start_number, end_number):
    list_numbers = []
    for eachnumber in range(start_number, end_number):
        if eachnumber % 2 == 0:
            list_numbers.append(eachnumber)
    return list_numbers

def isOdd(start_number, end_number):
    list_numbers = []
    for eachnumber in range(start_number, end_number):
        if eachnumber % 2 != 0:
            list_numbers.append(eachnumber)
    return list_numbers

print("Even", isEven(4,15))
print("Odd", isOdd(4,15))