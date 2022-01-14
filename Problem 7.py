def checkIfPrime(num):
    import math

    #topRange=math.floor(math.sqrt(num))
    for i in range(2,num):
        if (num % i) == 0:
            print('False')
            return False
            break
        elif i==(num-1):
            print('True')
            return True
        else:
            continue

primeList=[2]
index=1
while len(primeList)<10001:
    if checkIfPrime(index):
        primeList.append(index)
    index+=1

lenPrimeList=len(primeList)
finalPrime=primeList[-1]
print(f'Final prime is {finalPrime} in {lenPrimeList}-th position.')
print(primeList)

