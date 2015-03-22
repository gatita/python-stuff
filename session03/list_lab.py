#!/usr/bin/env python

fruit = ["Apples", "Pears", "Oranges", "Peaches"]

def series1(fruit):
    fruit_copy = fruit[:]
    print fruit
    new_fruit = raw_input("What's another type of fruit? ")
    fruit_copy.append(new_fruit)
    print fruit_copy
    number = raw_input("Pick a number, 1 through %i. " % len(fruit_copy))
    print number + ': ' + fruit_copy[int(number)-1]
    fruit_copy = ['Grapes'] + fruit_copy
    print fruit_copy
    fruit_copy.insert(0, 'Kiwi')
    print fruit_copy

    for x in fruit_copy:
        if x[0] == 'P':
            print x
            
    return fruit_copy

foo = series1(fruit)



