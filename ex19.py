def cheese_and_crackers(cheese_count, box_crackers):
    print("you have a %d cheese"%cheese_count)
    print("you have a %d cracker box"% box_crackers)
    print("Man that's enpogh for a party")
    print("get a blanket.\n")

print("we can give the functions into numbers directly")
cheese_and_crackers(20, 30)

print("or we can variables froms our script")
amount_of_cheese=10
amount_of_crackers=50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("we can do even math inside")
cheese_and_crackers(10+20, 5+6)

print("and we can combine two, variable and math")
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000)