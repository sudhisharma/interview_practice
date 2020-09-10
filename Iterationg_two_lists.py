
# want a (letter, num) pair for each letter in "abcd" and each number in "1234"

my_list = []

for let in "abcd":
    for num in "1234":
        my_list.append((let,num))
print(my_list)


######### same uisng list comprehension ##################

new_list = [(let,num) for let in "abcd" for num in range(1,5)]
print(new_list)