import math
def divCounter(n):
    nSqrt=math.floor(math.sqrt(n))
    factorList=[]

    for den in range(1,nSqrt+1):
        if n%den==0:
            factor=n/den
            factorList.append(factor)
            factorList.append(den)

    #factorList.sort()
    return factorList
