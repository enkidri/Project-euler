sumSquare=0
squareTotSum=0
for i in range(1,101):
    sumSquare+=i**2
    squareTotSum+=i
squareTotSum=squareTotSum**2
print(sumSquare)
print(squareTotSum)
diff=squareTotSum-sumSquare
print(diff)
