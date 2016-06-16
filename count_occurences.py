import urllib2
import sys 

print len(sys.argv)

if len(sys.argv) == 2:
    word = str(sys.argv[1])
else:
    word = 'python'

site = "https://en.wikipedia.org/wiki/Monty_Python"

contents = urllib2.urlopen(site).read().lower()

split = contents.split(' ')
# print split

print "Number of monty:"
print split.count('monty')

print "Number of " + word +":"
print split.count(word) 