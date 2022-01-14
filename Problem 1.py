i=0
iList=[]
for number in range(1000):
    if number%3==0 or number%5==0:
        i+=number
        iList.append(number)
    else:
        continue

print(i)
#print(iList)
