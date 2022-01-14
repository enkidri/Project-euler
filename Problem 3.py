import math
import time

factoredNumber=600851475143
end=math.floor(math.sqrt(factoredNumber))
factorList=[]
iList=[]
i=2
while True:
    if factoredNumber%i==0:
        factoredNumber=factoredNumber/i
        end=math.floor(math.sqrt(factoredNumber))
        #end=factoredNumber/2
        i+=1
        iList.append(i)
        factorList.append(factoredNumber)
        print('Found division ' +str(i))
        #time.sleep(2)
    elif i>=end:
        break
    else:
        i+=1
        print(i)

print('the final answer is ' +str(factorList[-1]))
print(factorList)
print(iList)

