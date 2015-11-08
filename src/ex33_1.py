def generate_list(n, s=1):
    i = 0
    numbers = []

    while i < n:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + s
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    return numbers

print generate_list(4, 2)
