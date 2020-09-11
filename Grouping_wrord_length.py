# Group the names based on there length if charectors

names =  ['raymond','rachel','matthew','roger','betty','melissa','judith','charlie']

new_dic = {}

for name in names:
    key = len(name)

    if key not in new_dic:
        new_dic[key] = [name]
    else:
        new_dic[key].append(name)

print(new_dic)
"""
name = raymond 
key = 7
new_dic = {7:['raymond']

# second
name = rachel
key = 6
new_dic = {7:['raymond'],6:['rachel']
"""