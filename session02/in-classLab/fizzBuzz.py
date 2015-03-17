def fizzBuzz():
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print 'FizzBuzz'
        elif i % 3 == 0:
            print 'Fizz'
        elif i % 5 == 0:
            print 'Buzz'
        else:
            print i
            
def fizzBuzz2():
    for i in range(1,101):
        if not i%3 and not i%5:
            print 'FizzBuzz'
        elif not i%3:
            print 'Fizz'
        elif not i%5:
            print 'Buzz'
        else:
            print i
            


    
    