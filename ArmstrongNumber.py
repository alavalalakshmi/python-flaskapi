def ArmstrongNumberChecker(a:str) ->bool:
    p = 0
    for idx in range(0, len(a)):
        p = p + int(a[idx])**3

    if int(a)==p:
        return True
    else:
        return False

