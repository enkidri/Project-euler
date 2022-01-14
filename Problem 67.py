#same as problem 18

with open('p067_triangle.txt', 'r') as fileObj:
    triangle=fileObj.read()

def triToList(tri):
    triSplit=tri.split("\n")
    triList=[]
    for row in triSplit:
        new=row.split(" ")
        triList.append(new)
    return triList

nrList=triToList(triangle)

for i in range(1, len(nrList)):
    rowAmount=len(nrList)-1 #last index of nrList
    lastRow=rowAmount-i
    print(lastRow)
    for iRow in range(len(nrList[lastRow])):
        nrList[lastRow][iRow]=int(nrList[lastRow][iRow])
        nrList[lastRow][iRow]+=max([int(nrList[lastRow+1][iRow]), int(nrList[lastRow+1][iRow+1])])

#print(*nrList, sep="\n")
finalAnswer=nrList[0]
print("The final answer is ", *finalAnswer)
