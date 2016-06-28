import requests
import sys 

print "# of command line args: ", len(sys.argv)

if len(sys.argv) == 2:
    word = str(sys.argv[1])
else:
    word = 'python'

url = 'https://en.wikipedia.org/wiki/Monty_Python'

r = requests.get(url)

content = r.content.lower() 

print "Number of monty: ", content.count('monty')
print "Number of " + word +": ", content.count(word) 


