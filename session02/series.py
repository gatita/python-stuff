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
        return 0
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
    