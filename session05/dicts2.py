#1 Print dict by passing it to a string format method

food_prefs = {"name": u"Grace",
              u"city": u"Seattle",
              u"cake": u"chocolate",
              u"fruit": u"mango",
              u"salad": u"greek",
              u"pasta": u"pesto"}


print "{name} is from {city}, and she likes {cake} cake, {fruit} fruit, {salad} salad, and {pasta} pasta.".format(**food_prefs)

#2 Use list comprehension to build a dict of the numbers 0-15
#  and their hexadecimal equivalents

l1 = range(16)
l2 = [hex(i) for i in l1]

hex1 = dict(zip(l1, l2))

print hex1

#3 Same as above using dict comprehension

hex2 = {i: hex(i) for i in range(16)}

print hex2

#4 Using food_prefs, make a dictionary using the same keys but 
#  with the number of 'a's in each value.

food = {k: k.count('a') for k in food_prefs.values()}

print food

#5 Create sets s2, s3, and s4 that contain the numbers 0-20 that are
#  divisible by 2, 3, and 4

s2 = {i for i in range(21) if not i % 2}
s3 = {i for i in range(21) if not i % 3}
s4 = {i for i in range(21) if not i % 4}
print s2, s3, s4

# More than 3? Create a sequence that holds all three sets
# Loop through the sequence to build the sets

my_sets = []

def create_multiples(x, y):
    #Create sequence of sets of multiples in range x through y
    my_sets = []
    for i in range(x, y):
        my_set = {num for num in range(21) if not num % i}
        my_sets.append(my_set)
    print my_sets

create_multiples(2,5)

# Extra Credit: Do the same as a one-liner, nesting a set coprehension
# inside a list comprehension

s2, s3, s4 = [{i for i in range(21) if not i % j} for j in range(2, 5)]
print s2, s3, s4






