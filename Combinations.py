class Combinations:
    def get_combinations(self, input):
        cnt = len(input)
        combinationsCnt = 2**cnt - 1
        for i in range(1, combinationsCnt+1):
            binCode = bin(i)[2:]
            binLength = len(binCode)
            appendZerosCnt = cnt - binLength
            binCodeStr = '0'*appendZerosCnt+binCode
            combinationStr = ''
            for j in range(0,cnt):
                if int(binCodeStr[j]) == 1:
                    combinationStr = combinationStr + input[j]
            print(combinationStr)

