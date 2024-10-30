def PalindromeChecker(input:str) -> bool:
    x = input[::-1]
    if input == x:
        return True
    else:
        return False