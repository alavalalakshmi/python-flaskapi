from PrimeNumber import PrimeNumberChecker

def prime_number_generator(lowerLimit:int, upperLimit:int):
    primeNumbers = []
    for i in range(lowerLimit,upperLimit+1):
        if PrimeNumberChecker(i):
            primeNumbers.append(i)
    print(primeNumbers)


