#Files!

f = open('test.txt', 'w') # w for overwrite
f.write('This file is now at Galvanize')
f.close()

f = open('test.txt')
s = f.read()
print s 
f.close() 