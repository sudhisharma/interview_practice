# script to check the letter count in a given string

str1 = "sudheendra"
str2 = "aa"

def string_count(string1):
    new_dict= {}
    for i in string1:
        new_dict[i] = string1.count(i)
    return new_dict

print(string_count(str1))
print(string_count(str2))


########################### without using the count ###############################

def letter_count(string1):
    new_dict = {}
    for i in string1:
        if i not in new_dict:
            new_dict[i] = 1
        else:
            new_dict[i] += 1

    return new_dict

print(letter_count(str2))