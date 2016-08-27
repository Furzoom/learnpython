from sys import argv

script, filename = argv

print "Now, I'm reading file %r." % filename

print "Reading the file..."
target = open(filename, 'r')
content = target.read()
print content

print "Closing %r." % filename
target.close()
