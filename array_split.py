from subprocess import list2cmdline


def splitArray(list_number, split_num):
    first_half = list_number[:split_num]
    for poping in range(0, split_num):
        list_number.pop(0)
    return first_half

def AppendArray(list_number,first_half):
    list_number.extend(first_half)
    return list_number

list_number = [1,12,13,14]
first_half=splitArray(list_number,1)
print (AppendArray(list_number,first_half))

