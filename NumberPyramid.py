import math

def number_pyramid_generator():
    pyramidHeight = 5
    totalSpaces = 5+(5-1)
    pyramidNumber = 0
    spaces = 0
    print("\n".strip())
    for i in range(1,6):
        cnt = i
        pyramidNumbers =''
        while(cnt>0):
            pyramidNumber+=1
            pyramidNumbers+=str(pyramidNumber)
            cnt-=1
            if cnt>0:
                pyramidNumbers+=' '
        spaces = totalSpaces-(i+i-1)
        outsideSpaces = math.floor(spaces/2)
        print(' '*outsideSpaces+pyramidNumbers+' '*outsideSpaces)




