def tetration (a, n):
    if n == 0:
        return 1
    
    result = a

    for i in range (n - 1):
        result = a ** result
    return result