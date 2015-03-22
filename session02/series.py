#!/usr/bin/env python

def fibonacci(n):
    """Return the nth number in the Fibonacci sequence"""
    f1, f2 = 0, 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    for i in range(n-1):
        value = f1 + f2
        f1 = f2
        f2 = value
    return value

def fibRecursive(n):
    """Return the nth number in the Fibonacci sequence recursively"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibRecursive(n-1) + fibRecursive(n-2)
        
def lucas(n):
    """Return the nth number in the Lucas sequence"""
    f1, f2 = 2, 1
    if n == 0:
        return 2
    elif n == 1:
        return 1
    for i in range(n-1):
        value = f1 + f2
        f1 = f2
        f2 = value
    return value
    
def fibLucas(n):
    """Return the nth number in the Lucas sequence recursively"""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return fibLucas(n-1) + fibLucas(n-2)
        
def sum_series(n, x=0, y=1):
    """Return the nth number in the Fibonacci or Lucas sequence.
    
    Produces numbers from the Fibonacci sequence when
    called with no optional parameters.
    
    Produces numbers from the Lucas sequence, when called with 
    the optional parameters x=2, y=1.
    """
    if x == 0 and y == 1:
        f1, f2 = 0, 1
        if n == 0:
            return 0
        elif n == 1:
            return 1
    elif x == 2 and y == 1:
        f1, f2 = 2, 1
        if n == 0:
            return 2
        if n == 1:
            return 1
    for i in range(n-1):
        value = f1 + f2
        f1 = f2
        f2 = value
    return value
    
if __name__ == "__main__":
    #test fibonacci 
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    
    #test lucas
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(2) == 3
    assert lucas(3) == 4
    assert lucas(4) == 7
    assert lucas(5) == 11
    assert lucas(6) == 18
    assert lucas(7) == 29
    
    #test sum_series
    assert sum_series(0) == 0
    assert sum_series(1) == 1
    assert sum_series(2) == 1
    assert sum_series(3) == 2
    assert sum_series(4) == 3
    assert sum_series(7) == 13
    assert sum_series(0, 2, 1) == 2
    assert sum_series(1, 2, 1) == 1
    assert sum_series(2, 2, 1) == 3
    assert sum_series(3, 2, 1) == 4
    assert sum_series(7, 2, 1) == 29