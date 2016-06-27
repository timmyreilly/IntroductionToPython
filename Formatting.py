from datetime import datetime

x = 12345.2345

print "x={:.2f}".format(x)

print "{:.3f}".format(x)

# Datetime Formatting 
d = datetime.now() 
print "{:%Y-%m-%d %H:%M:%S}".format(d) 
