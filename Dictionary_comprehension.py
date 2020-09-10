
# output ;-
# {'Bruce' : 'Batman' ,'wade' :Deadpool' , 'Logan':'wolverine' .....}

names = ['Bruce','clark','Peter','Logan','wade']
heros = ['Batman','Superman','Spiderman','Wolverine','deadpool']

new_dict = {}

for name,hero in zip(names,heros):
    new_dict[name ] = hero
print(new_dict)

################## Dict comprehension ########################

new_dict_dc = {name:hero for name, hero in zip(names,heros)}
print(new_dict_dc)

# To exclude perter fro the dict

new_dict_dcE = {name: hero for name, hero in zip(names,heros) if name !='Peter' }
print(new_dict_dcE)