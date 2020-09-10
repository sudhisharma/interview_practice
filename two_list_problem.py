#place the elements from the two string one after the other

"""
input : -
l1 = "abc"
l2 = 123
output :- a1b2b3

"""
l1 = "abc"
l2 = "123"

def com_values(list1,list2):
    if not list1 :
        return list2
    elif not list2:
        return list1
    else:
        return list1[i] + list2[i]


def combining(list1,list2):
    new_list = []
    for i in range(len(list1)):
        value = list1[i] + list2[i]
        new_list.append(value)
    return "".join(new_list)

print(combining(l1,l2))

