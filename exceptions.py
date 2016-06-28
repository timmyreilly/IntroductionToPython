l = [1, 2, 3]

l[4] 

x = [1, 2, 3]

try:
    x[8]
except:
    print("out of range")
else:
    print("in range") 


# Collecting data from Exception
try:
    x[8]
except Exception as e:
    print("out of range")
    print(e)
else:
    print("in range") 




