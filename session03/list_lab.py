#!/usr/bin/env python

fruit = ["Apples", "Pears", "Oranges", "Peaches"]

def series1(fruit):
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
            
    return fruit

fruit = series1(fruit)

def series2(fruit):
    fruit_copy = fruit[:]
    print fruit_copy
    fruit_copy.pop()
    print fruit_copy
    bad_fruit = raw_input("Pick a fruit from the list to delete. ")
    fruit_copy.remove(bad_fruit)
    print fruit_copy
    
    #bonus
    fruit_copy = fruit_copy * 2
    bad_fruit2 = raw_input("Pick a fruit, any fruit. ")
    while bad_fruit2 not in fruit_copy:
        bad_fruit2 = raw_input("Pick another fruit. ")
    for fruit in fruit_copy:
        if fruit == bad_fruit2:
            fruit_copy.remove(bad_fruit2)
    print fruit_copy
    
series2(fruit)

def series3(fruit):
    fruit_copy = fruit[:]
    for fruit in fruit_copy[:]:
        x = raw_input('Do you like %s? ' % fruit.lower())
        while x != 'no' and x != 'yes':
            x = raw_input('Please answer "yes" or "no". ')
        if x == 'no':
            fruit_copy.remove(fruit)
    print fruit_copy
    
series3(fruit)
        