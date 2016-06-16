names = ["Alfred", "Melinda", "Kramer", "Tobias", "Edmundo", "Zelda"]

for (i, x) in enumerate(names):
    print(i, x) 

print names 

names.sort() 

print names 

print [x.upper() for x in names]
