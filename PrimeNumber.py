def PrimeNumberChecker(n:int) -> bool:
    cnt = 0
    for i in range(1,n+1):
        x = n%i
        if x == 0:
            cnt += 1

    if(cnt == 2):
        return True
    else:
        return False

 