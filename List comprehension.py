nums  = [1,2,3,4,5,6,7,8,9]

my_list = []

for i in nums:
    my_list.append(i*i)
print(my_list)

my_list_lc = [n*n for n in nums]
print(my_list_lc)

################ same with map and lambda ########################

new_list =map(lambda n:n*n , nums)

print(new_list) # print map object

print(list(new_list)) # prints a list

############ To get the even numbers #######################

my_even_lists= [n for n in nums if n % 2 ==0]
print(my_even_lists)

############### same using filter and lambda ############
my_even_lists_fl = filter(lambda n: n%2 ==0 , nums)
print(my_even_lists_fl) # prints filter object
print(list(my_even_lists_fl))