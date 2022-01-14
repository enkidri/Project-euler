def factorial(nr):
    fctrl=1
    for i in range(1,nr+1):
        fctrl*=i
    return fctrl

sumOfDigit=0
fctrlStr=str(factorial(100))
for digit in fctrlStr:
    currentDigit=int(digit)
    sumOfDigit+=currentDigit

print(f'Sum of digits is {sumOfDigit}')

