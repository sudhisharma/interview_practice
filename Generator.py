
import random
# generators in Python
# nums = [1,2,3,4,5,6,7,8,9,10]
# def gen_fucn(nums):
#     for n in nums:
#         yield n*n
#
# my_gen = gen_fucn(nums)
# print(my_gen) # print generator object
#
# #print(next(my_gen))
# for i in my_gen:
#     print(i)
#
# ############################ same thing with generator comprehension ################
# my_gen_c = (n*n for n in nums)
#
# for i in my_gen_c:
#     print(i)

#######################Another Example ###############################

names = ['sudhi','lakshman','sandeep']
majors = ['teacher','engineer','doctor']

def people_gen(number_times):
    for i in range(number_times):
        people = {
            'id': i,
            'name' : random.choice(names),
            'major' : random.choice(majors)
                }
        yield people

my_people =people_gen(10)
print(my_people)
for i in my_people:
    print(i)

####################### Example 3 #########################

#Reversing the string

def rev_string(my_str):
    for i in range(len(my_str)-1 , -1 , -1):
        yield my_str[i]
for char in rev_string("Hello"):
    print(char)
