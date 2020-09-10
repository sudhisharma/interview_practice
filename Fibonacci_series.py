# Uisng the generator

def fibonacci_gen(nums):
    a,b = 0,1
    for i in range(nums):
        a,b = b, a+b
        yield a

# for i in fibonacci_gen(2):
#     print(i)


############### without generators ###############

num = 1
a,b = 0,1
for i in range(num):
    print(a)
    a,b = b, a+b