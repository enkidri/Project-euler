import time

gridSize=20
n=gridSize+1 #Node size
grid=[]

for i in range(n):
    if i==0:
        row=[1 for value in range(n)]
    else:
        row=[1]+[0 for value in range(n-1)]
    grid.append(row)

gridLen=len(grid[1])
row=1
while grid[gridLen-1][gridLen-1]==0:
    for i in range(1, gridLen):
        grid[row][i]=grid[row][i-1]+grid[row-1][i]
    row+=1

finalAnswer=grid[gridLen-1][gridLen-1]
print(f"The number of paths is {finalAnswer}.")
