#If all the numbers from 1 to 1000 (one thousand)
#inclusive were written out in words, how many letters would be used?

#Comment: badly written as is, unreadable

def nrToTextLen(nr):
    oneDigNum=[
    'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
    ]
    twoDigNum=[
    'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen','eighteen', 'nineteen',
    'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety',
    ]
    threeDigNum='hundred'
    fourDigNum='thousand'
    if len(str(nr))==1:
        digLen=len(oneDigNum[nr-1])
    elif len(str(nr))==2:
        if nr<20:
            digLen=len(twoDigNum[nr-10])
        elif nr>=20:
            frstDig=int(str(nr)[0])
            secondDig=int(str(nr)[1])
            if secondDig==0:
                digLen=len(twoDigNum[frstDig+8])
            else:
                digLen=len(twoDigNum[frstDig+8]+oneDigNum[secondDig-1])
    elif len(str(nr))==3:
        dig1=int(str(nr)[0])
        dig2=int(str(nr)[1])
        dig3=int(str(nr)[2])
        nrStr=str(nr)
        if dig3==0 and dig2==0:
            digLen=len(oneDigNum[dig1-1] + threeDigNum)
        elif dig3!=0 and dig2==0:
            digLen=len(oneDigNum[dig1-1] + threeDigNum + 'and' + oneDigNum[dig3-1])
        elif dig3==0 and dig2!=0 and dig2!=1:
            digLen=len(oneDigNum[dig1-1] + threeDigNum + 'and' + twoDigNum[dig2+8])
        elif dig2==1:
            if dig3==0:
                digLen=len(oneDigNum[dig1-1] + threeDigNum + 'and' + twoDigNum[0])
            else:
                digLen=len(oneDigNum[dig1-1] + threeDigNum + 'and' + twoDigNum[int(nrStr[1:])-10])
        else:
            digLen=len(oneDigNum[dig1-1] + threeDigNum + 'and' + twoDigNum[dig2+8]+oneDigNum[dig3-1])
    elif nr==1000:
        digLen=len('onethousand')
    return digLen


sumTxtNr=0
for value in range(1,1000+1):
    sumTxtNr+=nrToTextLen(value)
print(f'The total sum of the length of characters in numbers is {sumTxtNr}')
