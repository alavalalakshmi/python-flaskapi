def factorialOfNumber(n:int) -> int:
    x = 1
    while n>=1:
        x = x*n
        n = n-1
    return x