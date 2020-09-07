#Search a element in a list and provide the index

list1 = [1,4,8,5,6,0,3]

def search_value(sequence,value):
    count = 0
    length = len(sequence) #7
    while count<length :
        if sequence[count] == value:
            break
        else:
            count +=1

    if count == length:
        return None
    return count

print(search_value(list1,10))

########################## Using inbult function ##################################
def using_inbuild(sequence,value):
    for i,j in enumerate(sequence):
        if j == value:
            return i

print(using_inbuild(list1,10))