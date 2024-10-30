# Factorial
# Find the odd word - abc cde fgj bcd  
# ace bdf ceg hkl
# Create separate file for each program
# also include main function
# Todo combinations for given text ex:abc -> a b c ab bc ca bca cab 2** -1 =8 combinations 
from Sorting import Sorting
from Combinations import Combinations
from Factorial import factorialOfNumber
from OddWordInSeries import OddWordOutFromSeries
from Palindrome import PalindromeChecker
from PrimeNumber import PrimeNumberChecker
from ArmstrongNumber import ArmstrongNumberChecker
from FibonacciSeqGenerator import FibSeqGen
from AnagramChecker import anagram_string_checker
from PerfectNumber import perfect_number_checker
from PrimeNumberGenerator import prime_number_generator
from ArmstrongNumberFinder import armstrong_number_generator
from NumberPyramid import number_pyramid_generator
from CreditCard import CreditCard
from CreditCard import GoldCard
from CreditCard import PlatinumCard
from CreditCard import SilverCard
from CreditCard import get_statement
def main():
    # n = input(" enter the factorial number ")
    # x = factorialOfNumber(int(n))
    # print(x)
    # OddWordOutFromSeries()

    # #palindrome checker
    # pstr = input(" enter the palindrome string you want to check")
    # b = PalindromeChecker(pstr)
    # if b:
    #     print("entered string is palindrome")
    # else:
    #     print("entered string is not palindrome")
    
    # #primeNumberChecker
    # p = input("enter the number to check if prime or not")
    # status = PrimeNumberChecker(int(p))
    # print(status)

    # #ArmstrongNumber
    # q = input("enter the number to check if Armstrong or not")
    # isArmStrongNumber = ArmstrongNumberChecker(q)
    # if isArmStrongNumber:
    #     print(q + " is Armstrong Number")
    # else:
    #     print(q + "is not Armstrong Number")

    # #Fibonacci Sequence Generator
    # r = input("enter fibonacci sequence term number")
    # fibonacciSequence = FibSeqGen(int(r))
    # print(fibonacciSequence)

    # anagramStr1,anagramStr2 = input("enter two strings to check if they are Anagram Strings").split(",")
    # anagram_string_checker(anagramStr1, anagramStr2)

    # isPerfectNumber = input("enter the number for which you want to check is perfect")
    # perfect_number_checker(int(isPerfectNumber))

    # lowerLimit,upperLimit = input("enter the range of prime numbers ").split(',')
    # prime_number_generator(int(lowerLimit), int(upperLimit))

    # range1,range2 = input("enter the range of armstrong numbers ").split(',')
    # armstrong_number_generator(int(range1), int(range2))

    # number_pyramid_generator()

    # numbersList = input("enter the list of numbers you wanted to sort ").split(",")
    # sortList = [int(number) for number in numbersList]
    # sort = Sorting()
    # sort.bubble_sort(sortList)

    # insertionNumbersList = input("enter the list of numbers you wanted to sort ").split(",")
    # insertionSortList = [int(number) for number in insertionNumbersList]
    # sort.insertion_sort(insertionSortList)

    # combinationStrings = Combinations()

    # combinationStr = input("enter the string for which you need combinations ")
    # combinationStrings.get_combinations(combinationStr)

    # cc = CreditCard(5000,453)
    # cc.get_statement()

    # gc = GoldCard(5000,789)
    # gc.get_statement()

    pc = PlatinumCard(5000,234)
    pc.get_statement()

    # get_statement(gc)

    get_statement(pc)

    

if __name__ == "__main__":
        main()