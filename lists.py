names = ["Alfred", "Melinda", "Kramer", "Tobias", "Edmundo", "Zelda", "Tim"]

print names 

# sorting 
names.sort() 

# finding length 
print names 
print "Lenght of names: ", len(names) 

# comprehension
print [x.upper() for x in names]

# enumerate
for (i, x) in enumerate(names):
    print(i, x) 

#removing items 
popped = names.pop()
print popped 
popped = names.pop(0)
print popped 

# iterating 
for x in names:
    print x 

# slicing 
l = names[3:-1]
print l 

