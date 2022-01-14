import time

i=0
fibList=[1,2]
fib=0
totalSum=0
timeStart=time.time_ns()
while fib<4*10**6:
    fib=fibList[i] + fibList[i+1]
    fibList.append(fib)
    i+=1
    if fib%2==0:
        totalSum+=fib
timeEnd=time.time_ns()
timeDelta=timeEnd-timeStart
timeDelta_ms=timeDelta/(10**6)
print(f'It took {timeDelta_ms} ms to complete the calculation')
print(totalSum+2)

