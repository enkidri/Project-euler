import math

def factors(n):
    topRange=math.ceil(n/2)
    factors=[]
    for i in range(1, topRange+1):
        if n % i == 0:
            factors.append(i)
    return factors


amicableNr=[]

for currentNr in range(1, 10000+1):
    print(currentNr)
    factorList1=factors(currentNr)
    sumFactor1=sum(factorList1)

    factorList2=factors(sumFactor1)
    sumFactor2=sum(factorList2)

    if currentNr not in amicableNr and sumFactor2==currentNr and currentNr!=sumFactor1:
        amicableNr.append(currentNr)
        amicableNr.append(sumFactor1)

    else:
        continue
finalAnswer=sum(amicableNr)
print(f'The answer is {finalAnswer}')

