#!/usr/bin/env python

fruit = ["Apples", "Pears", "Oranges", "Peaches"]
print fruit
new_fruit = raw_input("What's another type of fruit? ")
fruit.append(new_fruit)
print fruit
number = raw_input("Pick a number, 1 through %i. " % len(fruit))
print number + ': ' + fruit[int(number)-1]
fruit = ['Grapes'] + fruit
print fruit
fruit.insert(0, 'Kiwi')
print fruit

for x in fruit:
    if x[0] == 'P':
        print x