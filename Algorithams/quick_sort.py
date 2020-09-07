# sorting the list into ascending order by quick sort techigue

"""
input = [1,3,7,4,9,5,1]
output =[1,1,3,4,5,7,9]

"""

list1 = [1,3,7,4,9,5,1]
list2 = [3,4,5,8,5,3]

def quick_sort(sequence):
    lenght= len(sequence)

    if lenght <= 1:
        return sequence
    else:
        low = []
        dup = []
        hight = []
        pivot = sequence.pop()
        for i in sequence:
            if i > pivot:
                hight.append(i)
            elif i== pivot:
                dup.append(i)
            else:
                low.append(i)
        return quick_sort(low) + dup +[pivot]+ quick_sort(hight)

print(quick_sort(list1))
print(quick_sort(list2))


#first iteration
# low = []
# dup = [1]
#high = [3,7,4,9,5]