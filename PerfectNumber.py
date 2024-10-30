import math

def perfect_number_checker(n:int):
    divisorsLimitNo = math.floor(n/2)
    divisors = 0
    for i in range(1,divisorsLimitNo+1):
        remainder = n%i
        if remainder == 0:
            divisors += i
        
    if divisors == n:
        print(str(n) + " is Perfect Number")
    else:
        print(str(n) + " is not a Perfect Number")
    