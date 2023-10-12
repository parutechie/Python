#from os import device_encoding
#import time
#import cProfile

def isAscending(list):
    isAscendingOrder=False
    index = 0
    while (index < len(list)-1):
        if (list[index]<=list[index+1]):
            isAscendingOrder=True
            index+=1
        else:
            isAscendingOrder = False
            break
    return isAscendingOrder

def isDesending(list):
    isDescendingOrder = False
    index=0
    while (index < len(list)-1):
        if (list[index]>=list[index+1]):
            isDescendingOrder=True
            index+=1
        else:
            isDescendingOrder = False
            break
    return isDescendingOrder

def isMonotonic(list):
    if (isAscending(list)):
        return True
    elif (isDesending(list)):
        return True
    return False

"""def looping():
    counter=0
    while(counter<100000000):
        counter+=1"""

"""list=[1,423,600,1234]
#start = time.time()
result=isMonotonic(list)
#end = time.time()
print ("isMonotonic ",list,": ",result)
#print("Execution time of the program is- ", (end-start)*1000000,"nano seconds")


#cProfile.run('isMonotonic(list)')
#cProfile.run('looping()')"""

