#Anagram strings examples ->'heart' and 'earth', 'python' and 'typhon'
def anagram_string_checker(str1:str, str2:str):
    sortedStr1 = sorted(str1)
    sortedStr2 = sorted(str2)
    anagramStrings = True

    if len(str1) != len(str2):
        print(str1+" and "+str2 +" are not anagram strings")
    else:
        for i in range(0,len(str1)):
            if ord(sortedStr1[i]) - ord(sortedStr2[i]) != 0:
                anagramStrings = False
                print(str1+" and "+str2 +" are not anagram strings")
                break
        if anagramStrings :
            print(str1+" and "+str2 +" are anagram strings")
            



