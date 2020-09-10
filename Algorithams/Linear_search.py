
# Search the element in a given list and return the index of the key

def linear_search (alist, key):
    for i in range(len(alist)):
        if alist[i] == key:
            return i
    return -1

alist = input("Enter the list of elements \n ")
alist = alist.split()
alist = [int(x) for x in alist]

key = int(input("Enter the key to check \n"))
index = linear_search(alist,key)
if (index<0):
    print("Element is not found in the given list",alist)
else:
    print(key,"is presnt in the position",index+1)
