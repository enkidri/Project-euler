import math
from itertools import *

def factors(n):
    topRange=math.ceil(n/2)
    factors=[]
    for i in range(1, topRange+1):
        if n % i == 0:
            factors.append(i)
    return factors

def is_abundant_sum(n):
    for i in abundantNr:
        if i > n:
            return False
        if (n - i) in abundantNr_set:
            return True
    return False

# def combinations(lst, n):
#     if n==0:
#         return [[]]
#     global abundantNr
#     global nrRange

#     l=[]
#     for i in range(0, len(lst)):
#         m = lst[i]
#         print('At number ', m)
#         remLst = lst[i + 1:]

#         for p in combinations(remLst, n-1):
#             sumVal=m+p[0]
#             l.append([m]+p)
#             if sumVal < topRange and sumVal in abundantNr:
#                 nrRange.remove(sumVal)
#     return l

topRange=28123
abundantNr=[]

for i in range(1,topRange):
    sumFactor=sum(factors(i))
    if sumFactor > i:
        abundantNr.append(i)
abundantNr=list(set(abundantNr))
abundantNr_set=set(abundantNr)

finalAnswer = sum(i for i in range(1, 28123 +1) if not is_abundant_sum(i))

# limit=len(abundantNr)
# abunComb=[]
# for i in range(len(abundantNr)+1):
#     for j in range(i, limit):
#         nrSum=abundantNr[i]+abundantNr[j]
#         if nrSum >= topRange:
#             limit = j
#             break
#         elif nrSum in nrRange:
#             nrRange.remove(nrSum)
#             print('Appending ', nrSum)


print(f'The final answer is {finalAnswer}')
