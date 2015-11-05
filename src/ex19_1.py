def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheese!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

amount_of_cheese = int(raw_input("cheese? "))
amount_of_crackers = int(raw_input("crackers? "))

cheese_and_crackers(amount_of_cheese, amount_of_crackers)
