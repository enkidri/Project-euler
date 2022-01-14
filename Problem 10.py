import math

def checkIfPrime(num):
    if num>100:
        top=math.floor(math.sqrt(num))
        bottom=math.floor(num/2)
    else:
        top=num
        bottom=2

    for i in range(bottom,top):
        if (num % i) == 0:
            return False
            break
        elif i==(top-1):
            return True
        else:
            continue

primeLim=2*10**6
sum=2
for i in range(2, primeLim+1):
    print(f'Current value: {i}')
    if checkIfPrime(i):
        sum+=i
print(f'The total sum is {sum}.')

