# Find the odd word - abc cde fgj bcd  
# ace bdf ceg hkl

def OddWordOutFromSeries():

    # z = ['abc', 'cde', 'fgj', 'bcd']
    # z = ['ace', 'bdf', 'ceg', 'hkl']
    z = ['abe', 'bcf', 'cdg', 'hjl']
    diff = ''
    series = []
    seriesWithDiff = {}

    for i in z:
        x = i
        # y = x[::-1]
        q = 100
        for idx in range(1, len(x)):
            p = ord(x[idx]) - ord(x[idx - 1])
            diff+=str(p)
        seriesWithDiff[i] = diff
        diff = '' 
    cnt = 0
    firstEle=''
    lastEle=''
    for i in range(1, len(seriesWithDiff)):
         if seriesWithDiff[z[i]] != seriesWithDiff[z[i-1]]:
            cnt += 1
            if cnt == 1:
                if i-1 == 0:
                    firstEle = z[i-1]
                elif i ==  len(seriesWithDiff)-1:
                    lastEle = z[i]
            elif cnt == 2:
                oddEle = z[i-1]

    if cnt == 2:
        print(oddEle + " is the odd one in the series")
    if cnt ==1:
        if len(firstEle) > 0:
            print(firstEle + " is the odd one in the series")
        elif len(lastEle) > 0:
            print(lastEle + " is the odd one in the series")

  
            
        
    
