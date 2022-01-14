import math
import time

palinNr=9009
largestNr=999*999

def checkPalin(nr):
    reverse=str(nr)[::-1]
    if int(reverse)==nr:
        return True
    else:
        return False

searchRegion=math.ceil(largestNr/2)
z=0
palinList=[]
for i in range(largestNr):
    currentNr=largestNr-i
    if z==1:
        break
    elif checkPalin(currentNr):
        print('checking palin')
        for i in range(100,1000):
            foundDiv=currentNr/i
            if currentNr%i==0 and len(str(int(foundDiv)))==3:
                z=1
                print(f'The factors is {foundDiv} and {i}')
                break

    else:
        print('no palin')
        continue


print('program finished')





