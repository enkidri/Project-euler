import time

collatzList={}
sqnLens={}

for i in range(13, 20):
    collaz=i
    collazList=[]
    print("Current collaz:", collaz)
    while True:
        if collaz%2==0:
            collaz=collaz/2
            collazList.append(collaz)
        elif collaz in collatzDict.keys():
            collazList.extend(collatzDict[collaz])
            collatzDict[i]=collazList
            break
        elif collaz==1:
            collatzDict[i]=collazList
            break
        else:
            collaz=3*collaz+1
            collazList.append(collaz)

    sqnLen=len(collazList)
    sqnLens[i]=sqnLen

print(collatzDict)

largestCollaz=max(sqnLens, key=sqnLens.get)
maxCollaz=sqnLens[largestCollaz]
print(f"With number {largestCollaz}, it produces the largest collaz sequence with the length of {maxCollaz}.")
