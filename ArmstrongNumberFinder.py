from ArmstrongNumber import ArmstrongNumberChecker

def armstrong_number_generator(lowerLimit:int,upperLimit:int):
    armstrongNumbers = []
    for i in range(lowerLimit,upperLimit+1):
        if ArmstrongNumberChecker(str(i)):
            armstrongNumbers.append(i)

    print(armstrongNumbers)


