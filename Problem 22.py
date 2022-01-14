import string

with open('p022_names.txt', 'r') as fileObj:
    nameStr=fileObj.read()

nameStr=nameStr.replace('"', "")
names=nameStr.split(',')
names.sort()

def score(nameList):
    alphabet=string.ascii_uppercase
    alphabetList=list(alphabet)
    index=1
    totScore=0
    for name in nameList:
        score=0
        for letter in name:
            orderNr=alphabetList.index(letter)+1
            score+=orderNr
        score*=index
        index+=1
        totScore+=score
    return totScore

finalAnswer=score(names)
print(f'The final answer is {finalAnswer}')
