my_name = 'Y. Ma'
my_age = 22 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

#print "Let's talk about %s." % my_name
#print "He's %d inches tall." % my_height
#print "He's %d pounds heavy." % my_weight
#print "Actually that's not too heavy."
#print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
#print "His teeth are usually %s depeding on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
#print "if I add %d, %d, and %d I get %d." % (
#        my_age, my_height, my_weight, my_age + my_height + my_weight)

# print with %r
print '%r' % my_hair
print '%c' % 'A'

print '%c' % 69
print '{:b}'.format(123)
print '{:3.3g}'.format(123.456789)
print '{:3.4g}'.format(123456.789)
