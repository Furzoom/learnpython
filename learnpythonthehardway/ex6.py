# define string x 
x = "There are %d types of people." % 10

# define string binary
binary = "binary"
# define string do_not
do_not = "don't"
# define string y
y = "Those who know %s and those who %s." % (binary, do_not)

# print x
print x
# print y
print y

# print with %r
print "I said: %r." % x
# print with %s
print "I also said: '%s'." % y

# define boolean hilarious
hilarious = False
# define string joke_evaluation
joke_evaluation = "Isn't that joke so funny?! %r"

# print something
print joke_evaluation % hilarious

# define string w
w = "This is the left side of..."
# define string e
e = "a string with a right side."

# print w + e
print w + e

