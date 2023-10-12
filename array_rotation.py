list=[10, 0,1,-4,3,9,7,6,2,7] # [4,1,2,3]
#list[0]->list[1]->list[2]->list[3]->list[0]

def shift_clockwise(list, index_to_occupy,value):
    if (index_to_occupy==0):
        list[index_to_occupy]=value
        return
    temp=list[index_to_occupy]
    list[index_to_occupy]=value
    if (index_to_occupy+1 == len(list)):
        index_to_occupy = 0
    else:
        index_to_occupy +=1
    print ("index_to_occupy: ",index_to_occupy, ", temp: ",temp)
    shift_clockwise(list, index_to_occupy,temp)

print("Before clockwise shift: ", list)
for counter in range(1,4):
    shift_clockwise (list,1,list[0])
    print ("After clockwise shift [",counter,"]: ", list)
